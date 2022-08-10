<template>
    <div class="container">
        <div class="row justify-content-md-center">
            <div class="col col-lg-10">
                <select id="doctor" class="form-select rounded-pill" v-model="doctor_v" @change="changeSchedule($event)" required>
                    <option disabled value="">Please select doctor</option>
                    <option v-for="doctor in doctors"
                    :key="doctor.id" :value="doctor.id">
                        {{doctor.firstName}} {{doctor.lastName}}
                    </option>
                </select>
                <div class=".col-md-3 .offset-md-3 linkSchedule">
                    <router-link :to="{ name: 'DoctorsScheduleCreate', param: { id : doctor_info.id }}" class="btn btn-light form-control rounded-pill">Add New Schedule</router-link>
                    <!-- <router-link :to="{ name: 'DoctorsScheduleEditList', param: { id : doctor_info.id }}" class="btn btn-light" ><i class="bi bi-calendar2-plus"></i></router-link> -->
                </div>
                <figure class="text-center">
                    <h3>{{doctor_info.firstName}}{{doctor_info.lastName}}'s Schedule List</h3>
                </figure>
                <table class="table table-bordered shadow p-3 mb-5 bg-body rounded tblSchedule">
                    <thead>
                        <tr>
                            <th class="thDay"></th>
                            <th v-for="day in dayValue"
                            v-bind:key="day.id"
                            class="thDay"
                            > {{ day.name }} </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="time in doctors_time" v-bind:key="time.id">
                            <td>{{time}}</td>
                            <td v-for="day in dayValue" v-bind:key="day.id">
                                <span v-for="schedule in doctors_schedule" v-bind:key="schedule.id">
                                    <span v-if="schedule.startTime+'-'+schedule.endTime == time && schedule.day == day.value">
                                    {{schedule.hospital_name}}<br>
                                    <p class="font-monospace">({{schedule.specialist}})</p>
                                    </span>
                                </span>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <div v-if="doctors_schedule.length == 0">
                    <p class="font-monospace fs-3 lblNoSchedule">There Is No Schedule for {{doctor_info.firstName}}{{doctor_info.lastName}}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { getAPI } from '../../axios-api'
    export default{
        name: 'DoctorsOneSchedule',
        data () {
            return {
                doctor_v: '',
                doctors_schedule: [],
                doctors_time: [],
                doctors: [],
                dayValue: [
                    {id: 1,value: "sunday", name: 'Sunday', disabled: false, flag: 0},
                    {id: 2,value: "monday", name: 'Monday', disabled: false, flag: 0},
                    {id: 3,value: "tuesday", name: 'Tuesday', disabled: false, flag: 0},
                    {id: 4,value: "wednesday", name: 'Wednesday', disabled: false, flag: 0},
                    {id: 5,value: "thursday", name: 'Thursday', disabled: false, flag: 0},
                    {id: 6,value: "friday", name: 'Friday', disabled: false, flag: 0},
                    {id: 7,value: "saturday", name: 'Saturday', disabled: false, flag: 0},
                ],
                doctor_info: {},
            }
        },
        mounted() {
            this.getOneSchedule()
        },
        methods:{
            async getOneSchedule(){
                const doctorID = this.$route.params.id
                console.log(doctorID)
                getAPI
                    .post(`doctors/doctor_schedule_list/${doctorID}`)
                    .then(response => {
                        console.log(response)
                        this.doctors_schedule=response.data[0]
                        console.log(this.doctors_schedule)
                        for(var ds of this.doctors_schedule){
                            this.doctors_time.push(ds.startTime+'-'+ds.endTime)
                        }
                        console.log(this.doctors_time)

                        this.doctors = response.data[1]
                        console.log(this.doctors)
                        for(var doctor of this.doctors){
                            if(doctor.id == doctorID){
                                this.doctor_info=doctor
                            }
                        }
                        console.log(this.doctor_info)
                    })
                    .catch(error => {
                        console.log('Fail')
                        if(error.response) {
                            for( const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } 
                        else if(error.message) {
                            this.errors.push('Something went wrong. Please Try Again')
                            console.log(error.message)
                        }
                    })
            },
            changeSchedule: function(event) {
                console.log(event.target.selectedOptions[0].value)
                window.location.href = ('/schedule_list/'+event.target.selectedOptions[0].value)
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

.form-select{
    background-color: rgb(245, 242, 242);
    width: 20%;
}
.lblNoSchedule{
    text-align: center;
    color: red;
}
.thDay{
    width: 10%;
    background-color: rgb(239, 229, 249);
}
.linkSchedule {
    margin-left: 80%;
}
</style>