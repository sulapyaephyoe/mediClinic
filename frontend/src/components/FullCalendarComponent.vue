<script>
import '@fullcalendar/core/vdom' // solves problem with Vite
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction'

import { getAPI } from '../../axios-api'

export default {
  components: {
    FullCalendar // make the <FullCalendar> tag available
  },
  data() {
    return {
      items:[],
      items1:[
      {'title': 'hello',
      'daysOfWeek': [1]}
      ],
      calendarOptions: {
        plugins: [ dayGridPlugin, interactionPlugin ],
        initialView: 'dayGridMonth',
        dateClick: this.handleDateClick,
        events: this.items,
      }
    }
  },
  beforeCreate() {
    this.items.push({'title': 'hello','daysOfWeek': [1]})
  },
  created() {
    this.detail_specialist('Dermatology')
  },
  methods: {
    handleDateClick: function(arg) {
      alert('date click! ' + arg.dateStr)
    },
    detail_specialist(sname){
      console.log(sname)
      getAPI.get(`schedule/get_schedule_data/${sname}`)
      .then(response => {
        this.join_data = response.data.join_data
        this.doctor_data = response.data.doctor_data
        this.hospital_data = response.data.hospital_data
        this.event_data()
      })
      .catch(error => {
          console.log(error)
      })
    },
    event_data() {

        this.join_data.forEach(element => {
        var k = this.dayKey(element.day)   
        this.items.push({
          'title': element.doctor_id,
          'daysOfWeek': [k]
        })  
      });     
      console.log('event========='+this.items)
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
    }
  }
}
</script>
<template>
<div class="container">
  <FullCalendar :options="calendarOptions" />
</div>
</template>
<style scoped>
.container {
  width: 800px;
  height: 800px;
}
</style>