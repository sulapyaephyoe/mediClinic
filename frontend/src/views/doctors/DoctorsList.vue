<template>
    <div class="container mt-5 mb-5">
        <div class="row">
            <div class="col">
                <router-link :to="{ name: 'DoctorsCreate'}" class="btn btn-light" >Create Doctor</router-link>
                <figure class="text-center">
                    <h3>Doctors List</h3>
                </figure>
                <table class="table">
                <thead>
                    <tr>
                        <th scope="col">First Name</th>
                        <th scope="col">Last Name</th>
                        <th scope="col">Gender</th>
                        <th scope="col">Specialist</th>
                        <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr 
                        v-for="doctor in doctors"
                        v-bind:key="doctor.id"
                    >
                        <td>{{ doctor.firstName }}</td>
                        <td>{{ doctor.lastName }}</td>
                        <td>{{ doctor.gender }}</td>
                        <td>{{ doctor.specialist }}</td>
                        <td>
                            <router-link :to="{ name: 'DoctorsEdit', params: { id : doctor.id }}" class="btn btn-light" ><i class="bi bi-pencil"></i></router-link>&thinsp;
                            <router-link :to="{ name: 'DoctorsOneSchedule', params: { id : doctor.id }}" class="btn btn-light" ><i class="bi bi-calendar2-week"></i></router-link>&thinsp;
                            <router-link :to="{ name: 'DoctorsScheduleEditList', params: { id : doctor.id }}" class="btn btn-light" ><i class="bi bi-calendar2-plus"></i></router-link>
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
        name: 'DoctorsList',
        data () {
            return {
                doctors: []
            }
        },
        mounted() {
            this.getDoctors()
        },
        methods:{
            async getDoctors(){
                getAPI
                .get('doctors/doctorslist')
                .then(response => {
                    this.doctors=response.data
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