<template>
    <div class="container">
        <div class="row justify-content-md-center">
            <div class="col col-lg-10">
                <figure class="text-center">
                    <h3>Doctors Schedule List</h3>
                </figure>
                <table class="table">
                <thead>
                    <tr>
                        <th scope="col">Hospital ID</th>
                        <th scope="col">Doctor ID</th>
                        <th scope="col">Day</th>
                        <th scope="col">Start Time</th>
                        <th scope="col">End Time</th>
                    </tr>
                </thead>
                <tbody>
                    <tr 
                        v-for="schedule in doctors_schedule"
                        v-bind:key="schedule.id"
                    >
                        <td>{{ schedule.hospital_id }}</td>
                        <td>{{ schedule.name }}</td>
                        <td>{{ schedule.specialist }}</td>
                        <td>{{ schedule.day }}</td>
                        <td>{{ schedule.startTime }}</td>
                        <td>{{ schedule.endTime }}</td>
                    </tr>
                </tbody>
                </table>

                <table class="table table-bordered table-hover tblSchedule">
                    <thead>
                        <tr>
                            <th></th>
                            <th> SunDay </th>
                            <th> MonDay </th>
                            <th> Tuesday </th>
                            <th> Wednesday </th>
                            <th> Thursday </th>
                            <th> Friday </th>
                            <th> Saturday </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>10:00-11:00</td>
                        </tr>
                        <tr>
                            <td>11:00-12:00</td>
                        </tr>
                        <tr>
                            <td>12:00-13:00</td>
                        </tr>
                        <tr>
                            <td>13:00-14:00</td>
                        </tr>
                        <tr>
                            <td>14:00-15:00</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            
            <div class="col-12">
                hhh
            </div>
        </div>
    </div>
</template>

<script>
import { getAPI } from '../../axios-api'
    export default{
        name: 'DoctorsSchduleList',
        data () {
            return {
                doctors_schedule: []
            }
        },
        mounted() {
            this.getDoctorsSchedule()
        },
        methods:{
            async getDoctorsSchedule(){
                getAPI
                .get('doctors/doctor_schedule_list')
                .then(response => {
                    console.log(response)
                    console.log(response.data.fields)
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
    background-color: aqua;
    text-align: center;
    padding-bottom: 3%;
}
.tblSchedule td{
    background-color: blueviolet;
    text-align: center;
    padding-top: 3%;
}
</style>