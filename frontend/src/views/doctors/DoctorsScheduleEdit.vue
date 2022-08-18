<template>
    <div class="container mt-5 mb-5">
        <div class="row">
            <div class="col-md-6 offset-md-3">
                <figure class="text-center">
                    <h3>{{ doctor_info.firstName }} 's Schedule Edit Form</h3>
                </figure>
                <form @submit.prevent="submitForm">
                    <div class="mb-3">
                        <label for="hospital" class="form-label">Hospital</label>
                        <input type="text" class="form-control" id="hospital" v-model="hospital" disabled>
                    </div>
                    <div class="mb-3">
                        <label for="day" class="form-label">Day</label>
                        <select class="form-select" aria-label="Default select example" v-model="day" required>
                            <option disabled value="">Please select day</option>
                            <option v-for="day in dayValue" 
                            :key="day.value" :value="day.value">
                                {{day.name}}
                            </option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="startTime" class="form-label">Start Time</label>
                        <input type="time" class="form-control" id="startTime" v-model="startTime" required>
                    </div>
                    <div class="mb-3">
                        <label for="endTime" class="form-label">End Time</label>
                        <input type="time" class="form-control" id="endTime" v-model="endTime" required>
                    </div>
                    <button type="submit" class="btn-style-one">Edit</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { getAPI } from '@/axios-api'

    export default{
        name: 'DoctorsScheduleEdit',
        data () {
            return {
                hospital: '',
                day: '',
                startTime:'',
                endTime:'',
                dayValue: [
                    {id: 1,value: "Sunday", name: 'Sunday', disabled: false, flag: 0},
                    {id: 2,value: "Monday", name: 'Monday', disabled: false, flag: 0},
                    {id: 3,value: "Tuesday", name: 'Tuesday', disabled: false, flag: 0},
                    {id: 4,value: "Wednesday", name: 'Wednesday', disabled: false, flag: 0},
                    {id: 5,value: "Thursday", name: 'Thursday', disabled: false, flag: 0},
                    {id: 6,value: "Friday", name: 'Friday', disabled: false, flag: 0},
                    {id: 7,value: "Saturday", name: 'Saturday', disabled: false, flag: 0},
                ],
                schedule: {},
                hospitalValue: [],
                doctorValue: [],
                doctor_info: {},
                hospital_id: 0
            }
        },
        beforeMount() {
            this.getHospital();
            this.getDoctor();
        },
        mounted() {
            this.getScheduleEdit()
        },
        methods:{
            async getHospital(){
                getAPI
                    .get('doctors/get_hospital')
                    .then(response => {
                        this.hospitalValue = response.data
                        console.log("vvv"+this.hospitalValue)
                        for(var h of this.hospitalValue){
                            console.log("HHH"+h.name)
                        }
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
            async getScheduleEdit() {
                const scheduleID = this.$route.params.scheduleid
                const doctorID = this.$route.params.doctorid
                getAPI
                    .get(`doctors/schedule_edit/${doctorID}/${scheduleID}`)
                    .then(response => {
                        console.log(response)
                        this.schedule = response.data[0]
                        for(var h of this.hospitalValue){
                            if(h.id == this.schedule.hospital_id){
                                this.hospital = h.name
                                this.hospital_id = h.id
                            }
                        }
                        this.day = this.schedule.day
                        this.startTime = this.schedule.startTime
                        this.endTime = this.schedule.endTime
                    })
            },
            async getDoctor(){
                getAPI
                    .get('doctors/doctorslist')
                    .then(response => {
                        console.log(response.data)
                        this.doctorValue = response.data
                        for(var v of this.doctorValue){
                            if(v.id == this.$route.params.doctorid){
                                this.doctor_info = v
                            }
                        }
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
            async submitForm() {
                const formData = {
                    doctor_id: this.$route.params.doctorid,
                    hospital_id: this.hospital_id,
                    day:  this.day,
                    startTime: this.startTime,
                    endTime: this.endTime
                }
                const scheduleID = this.$route.params.scheduleid
                const doctorID = this.$route.params.doctorid
                getAPI
                    .post(`doctors/schedule_update/${doctorID}/${scheduleID}`,formData)
                    .then(response => {
                        console.log('Success')
                        console.log(response)
                        alert("Data Updated Successfully!")
                        this.$router.push(`/schedule_edit_list/${doctorID}`)
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