<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <router-link :to="{ name: 'BookingCreate'}" class="btn btn-light" >Create Booking</router-link>
                <figure class="text-center">
                    <h3>Booking List</h3>
                </figure>
                <table class="table">
                <thead>
                    <tr>
                        <th scope="col">Patient</th>
                        <th scope="col">Email</th>
                        <th scope="col">Phone</th>
                        <th scope="col">DoctorType</th>
                        <th scope="col">Date Time</th>
                        <th scope="col">Fees</th>
                        <th scope="col">Service</th>
                    </tr>
                </thead>
                <tbody>
                    <tr 
                        v-for="booking in bookinglist"
                        v-bind:key="booking.id"
                    >
                        <td>{{ booking.patient }}</td>
                        <td>{{ booking.email }}</td>
                        <td>{{ booking.phone }}</td>
                        <td>{{ booking.doctortype }}</td>
                        <td>{{ booking.datetime }}</td>
                        <td>{{ booking.fee }}$</td>
                        <td>{{ booking.service }}</td>
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
        name: 'BookingList',
        data () {
            return {
                bookinglist: []
            }
        },
        mounted() {
            this.getBooking()
        },
        methods:{
            async getBooking(){
                getAPI
                .get('booking/bookinglist')
                .then(response => {
                    console.log(response)
                    this.bookinglist=response.data
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