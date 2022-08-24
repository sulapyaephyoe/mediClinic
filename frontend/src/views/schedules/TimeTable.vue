<template>
<div id="app" class="class"> 
  <div class="dropdown">
    <select class="form-select rounded-pill" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false" @change="detail_specialist($event)">
      <option disabled value="" selected>Please select specialist</option>
      <option v-for="data in specialist_data" v-bind:key="data.specialist">{{data.specialist}}</option>
    </select>
  </div>
  <FullCalendar :options="calendarOptions" />
  <br><br>
 </div>
</template>
<script>
import '@fullcalendar/core/vdom'
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
      specialist_data: [],
      join_data: [],
      doctor_data: [],
      hospital_data: [],

      calendarOptions: {
        plugins: [ dayGridPlugin, timeGridPlugin, interactionPlugin ],
        initialView: 'dayGridMonth',
        eventClick: this.showEventClick,
        dateClick: this.clearElement,
        events: [{'title': '','daysOfWeek': []}],
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
    setTimeout(this.clearElement, 10000);  
  },
  created() {
    this.get_specialist();
  },
  methods: {
    get_specialist() {
      getAPI.get('schedule/get_specialists')
      .then(response => {
          this.specialist_data=response.data
          console.log(this.specialist_data)
      })
      .catch(error => {
        console.log(error)
      })
    },
    
    detail_specialist(event) {
      let sname = event.target.selectedOptions[0].value
      this.calendarOptions.events = [{}]
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
        let content = hospital.name
        let k = this.dayKey(element.day)   
        this.calendarOptions.events = [ 
          ...this.calendarOptions.events, {
            title: content, 
            daysOfWeek: [k],
            startTime: element.startTime,
            endTime: element.endTime,
            extendedProps: {
              dname: "Dr."+ doctor.firstName + " " + doctor.lastName + "<br>from " + element.startTime + " to " + element.endTime
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
      console.log(arg.event)
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
.dropdown {
  margin: 20px 20px 40px 210px;
}
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
.form-select {
  background-color: rgb(245, 242, 242);
  width: 20%;
}
</style>