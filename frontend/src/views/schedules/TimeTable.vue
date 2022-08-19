
<template>
<div class="class">
  <FullCalendar :options="calendarOptions" />
  <span class="displayText" id="displayText">Hi I am ToolTip</span>
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
  components: {
    FullCalendar
  },
  data() {
    return {
      calendarOptions: {
        plugins: [ dayGridPlugin, timeGridPlugin, interactionPlugin ],
        initialView: 'dayGridMonth',
        eventClick: this.showEventClick,
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
        let content = "Dr."+ doctor.firstName + " " + doctor.lastName + " \r\nAt " + hospital.name + "hospital."
        let k = this.dayKey(element.day)   
        this.calendarOptions.events = [ 
          ...this.calendarOptions.events, {
            title: content, 
            daysOfWeek: [k]
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
      console.log(arg.event.title)
      var popup = document.getElementById("displayText");
      popup.classList.toggle("show");
    },
  }
}
</script>
<style scoped>
.class {
-webkit-user-select: none;
position: relative;
}
.displayText {
position: absolute;
bottom: -230%;
left: 50%;
margin-left: -80px;
width: 160px;
background-color: aqua;
color: #fff;
color: red;
text-align: center;
border-radius: 6px;
padding: 8px 0;
visibility: hidden;
}
.displayText::before {
content: "";
border-width: 5px;
border-style: solid;
top: -28%;
left: 45%;
border-color: transparent transparent yellow transparent;
position: absolute;
}
.show {
visibility: visible;
}
</style>