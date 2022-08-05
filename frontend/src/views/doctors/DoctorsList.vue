<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <figure class="text-center">
                    <h3>DoctorsList</h3>
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
                        <!-- <td>{{ doctor.id }}</td> -->
                        <td>
                            <router-link :to="{ name: 'DoctorsScheduleCreate', params: { id : doctor.id }}" class="btn btn-light" >Schedule</router-link>
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
                    console.log(response)
                    console.log(response.data.fields)
                    this.doctors=response.data
                    console.log(this.doctors)
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