<template>
    <div class="container mt-5 mb-5">
        <div class="row">
            <div class="col">
                <!-- <router-link :to="{ name: 'DoctorsScheduleCreate', params: { id : doctor.id }}" class="btn btn-light" >Schedule</router-link> -->
                <figure class="text-center">
                    <h3>{{ doctor.firstName }} {{ doctor.lastName }}'s Schedule List</h3>
                </figure>
                <table class="table">
                <thead>
                    <tr>
                        <th scope="col">Hospital</th>
                        <th scope="col">Day</th>
                        <th scope="col">Start Time</th>
                        <th scope="col">End Time</th>
                        <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr 
                        v-for="schedule in doctors_schedule"
                        v-bind:key="schedule.name"
                    >
                        <td><span v-for="hospital in hospitalValue" v-bind:key="hospital.id">
                                <span v-if="hospital.id == schedule.hospital_id">
                                    {{hospital.name }}
                                </span>
                            </span>
                        </td>
                        <td>{{ schedule.day }}</td>
                        <td>{{ schedule.startTime }}</td>
                        <td>{{ schedule.endTime }}</td>
                        <!-- <td>{{ schedule.id }}</td> -->
                        <td>
                            <router-link :to="{ name: 'DoctorsScheduleEdit', params: { doctorid : doctor.id , scheduleid : schedule.id }}" class="btn btn-light" ><i class="bi bi-pencil"></i></router-link>
                        </td>
                    </tr>
                </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import { getAPI } from '../../axios-api'
    export default{
        name: 'DoctorsScheduleEditList',
        data () {
            return {
                doctor: {},
                doctors_schedule: [],
                doctorValue: [],
                hospitalValue: [],
            }
        },
        mounted() {
            this.getDoctor()
        },
        methods:{
            async getDoctorSchedule(){
                const doctorID = this.$route.params.id
                console.log(doctorID)
                getAPI
                    .post(`doctors/schedule_edit_list/${doctorID}`)
                    .then(response => {
                        console.log(response)
                        this.doctors_schedule=response.data
                        console.log(this.doctors_schedule)
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
            async getDoctor(){
                getAPI
                    .get('doctors/doctorslist')
                    .then(response => {
                        console.log(response.data)
                        this.doctorValue = response.data
                        for(var v of this.doctorValue){
                            if(v.id == this.$route.params.id){
                                this.doctor = v
                            }
                        }
                        this.getHospital()
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
            async getHospital(){
                getAPI
                    .get('doctors/get_hospital')
                    .then(response => {
                        console.log(response.data)
                        this.hospitalValue = response.data
                        this.getDoctorSchedule()
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
            }
        }
    }
</script>