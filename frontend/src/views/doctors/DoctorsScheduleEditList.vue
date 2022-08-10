<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <!-- <router-link :to="{ name: 'DoctorsScheduleCreate', params: { id : doctor.id }}" class="btn btn-light" >Schedule</router-link> -->
                <figure class="text-center">
                    <h3>'s Schedule List</h3>
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
                        <td>{{ schedule.hospital_id }}</td>
                        <td>{{ schedule.day }}</td>
                        <td>{{ schedule.startTime }}</td>
                        <td>{{ schedule.endTime }}</td>
                        <td>
                            <router-link :to="{ name: 'DoctorsScheduleEdit', param: { id : schedule.id }}" class="btn btn-light" ><i class="bi bi-pencil"></i></router-link>
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
                doctorValue: []
            }
        },
        mounted() {
            this.getDoctor(),
            this.getDoctorSchedule()
        },
        methods:{
            async getDoctorSchedule(){
                const doctorID = this.$route.params.id
                console.log(doctorID)
                getAPI
                    .post(`doctors/schedule_edit/${doctorID}`)
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