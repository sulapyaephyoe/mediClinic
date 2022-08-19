<template>
    <div class="container">
        <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/css/bootstrap.min.css" rel="stylesheet" />
        </head>

        <div class="dropdown">
            <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                Select Specialist
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                <li v-for="data in specialist_data" v-bind:key="data.specialist">
                    <a class="dropdown-item" href="#" @click="detail_specialist(data.specialist)">{{data.specialist}}</a>
                </li>
            </ul>
        </div>

        <div>
            <CalendarComponent/>
        </div>
        <div class="schedule-table">
            <table class="table table-bordered shadow p-3 mb-5 bg-body rounded tblSchedule">
                <thead>
                    <tr><th></th><th v-for="day in dayValue" v-bind:key="day">{{day}}</th></tr>
                </thead>
                <tbody>
                    <tr v-for="indx in join_data" v-bind:key="indx.id">
                        <td>{{indx.startTime}}-{{indx.endTime}}</td>
                        <td v-for="day in dayValue" v-bind:key="day">
                            <div v-if="indx.day==day">
                                <p style="display:none">
                                    {{temp_var_doc= doctor_data.find(x => x.id === indx.doctor_id)}}
                                    {{temp_var_hos= hospital_data.find(x => x.id === indx.hospital_id)}}
                                </p>
                                {{temp_var_doc.firstName}} {{temp_var_doc.lastName}}<br>
                                <router-link to="/">{{temp_var_hos.name}}</router-link>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>              
</template>

<script>
import { getAPI } from '../../axios-api'
import CalendarComponent from '@/components/CalendarComponent';
export default {
    name: 'TimeTable',
    components: {
        CalendarComponent,
    },
    data() {
        return {
            specialist_data: [],
            join_data: [],
            doctor_data: [],
            hospital_data: [],
            dayValue: ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],
            temp_var_doc: '',
            temp_var_hos: '',
        }
    },
    created() {
        this.get_specialist()
    
    },
    methods: {
       get_specialist(){
        getAPI
            .get('schedule/get_specialists')
            .then(response => {
                this.specialist_data=response.data
                console.log(this.specialist_data)
            })
            .catch(error => {
                console.log(error)
            })
        },

        detail_specialist(sname){
            console.log(sname)
            getAPI.get(`schedule/get_schedule_data/${sname}`)
            .then(response => {
                this.join_data = response.data.join_data
                this.doctor_data = response.data.doctor_data
                this.hospital_data = response.data.hospital_data
                console.log(this.join_data)
                console.log(this.doctor_data.find(x => x.id === 1).specialist)
            })
            .catch(error => {
                console.log(error)
            })
        }
        
    }
}
</script>
<style scoped>

.tblSchedule {
    border: 1px solid #eee
}
.tblSchedule tr{
    height: 100px;
}
.tblSchedule th{
    text-align: center;
    padding-bottom: 3%;
}
.tblSchedule td{
    text-align: center;
    padding-top: 3%;
}

</style>