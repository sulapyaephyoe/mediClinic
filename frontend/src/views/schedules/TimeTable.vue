
<template>
<div id="app" class="class">
  <FullCalendar :options="calendarOptions" />
 </div>
</template>
<script>
import '@fullcalendar/core/vdom' // solves problem with Vite
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from "@fullcalendar/timegrid";
import interactionPlugin from '@fullcalendar/interaction'

import { getAPI } from '../../axios-api'

export default {
  el: '#app',
  components: {
    FullCalendar
  },
  data() {
    return {
      clickFlag: false,
      calendarOptions: {
        plugins: [ dayGridPlugin, timeGridPlugin, interactionPlugin ],
        initialView: 'dayGridMonth',
        eventClick: this.showEventClick,
        dateClick: this.clearElement,
        events: [{'title': 'hello','daysOfWeek': [0]}],
        headerToolbar: {
          left: "prev,next today",
          center: "title",
          right: "dayGridMonth,timeGridWeek,timeGridDay"
        },
      }
    }
  },
  beforeCreate() {
  },
  mounted: function () {
    //this.$el.addEventListener('click', this.clearElement)
    setTimeout(this.clearElement, 5000);  
  },
  created() {
    this.detail_specialist('Dermatology')
  },
  methods: {

    detail_specialist(sname){
      getAPI.get(`schedule/get_schedule_data/${sname}`)
      .then(response => {
        this.join_data = response.data.join_data
        this.doctor_data = response.data.doctor_data
        this.hospital_data = response.data.hospital_data
        this.add_event()
      })
      .catch(error => {
          console.log(error)
      })
    },

    add_event() {
      this.join_data.forEach(element => {
        let doctor = this.doctor_data.find(x => x.id === element.doctor_id)
        let hospital = this.hospital_data.find(x => x.id === element.hospital_id)
        // let content = "Dr."+ doctor.firstName + " " + doctor.lastName + " At " + hospital.name + " hospital."
        let content = hospital.name
        let k = this.dayKey(element.day)   
        this.calendarOptions.events = [ 
          ...this.calendarOptions.events, {
            title: content, 
            daysOfWeek: [k],
            startTime: element.startTime,
            endTime: element.endTime,
            extendedProps: {
              dname: "Dr."+ doctor.firstName + " " + doctor.lastName
            },
          }
        ];
      });     
    },

    dayKey(day) {
      var dkey=0;
      switch(day) {
        case 'Sunday': dkey=0;break;
        case 'Monday': dkey=1;break;
        case 'Tuesday': dkey=2;break;
        case 'Wednesday': dkey=3;break;
        case 'Thursday': dkey=4;break;
        case 'Friday': dkey=5;break;
        case 'Saturday': dkey=6;break;
      }
      return dkey;
    },

    showEventClick(arg) {
      this.clearElement();
      var btn = document.createElement("button");
      btn.id = "btnClick"  // background-color: #e1bc99;
      btn.setAttribute(
        'style',
        `position: absolute; 
        left: ${arg.jsEvent.pageX}px !important; 
        top: ${arg.jsEvent.pageY}px !important;
        width: 200px;
        height: 100px;
        z-index: 1;
        background-color: #fcdbbc;
        color: black;
        text-align: center;
        border-radius: 6px;
        border: 2px solid #e7e7e7;
        `,
      );  
      btn.innerHTML = arg.event.title+"<br>"+arg.event.extendedProps.dname;  
      document.body.appendChild(btn);  
    },
    clearElement() {
      if (document.contains(document.getElementById("btnClick"))) {
        document.getElementById("btnClick").remove();
      }
    }
  }
}
</script>
<style scoped>
.displayText {
  background-color: blue !important;
}
.container {
  position: relative !important;
  max-width: 1100px;
  margin: 0 auto;
}
.fc {
  /* the calendar root */
  max-width: 1100px;
  margin: 0 auto;
}
</style>