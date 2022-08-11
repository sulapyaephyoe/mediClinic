<template>
    <div class="container">
        <div class="row">
            <div class="col-md-6 offset-md-3">
                <figure class="text-center">
                    <h3>Schedule Edit Form</h3>
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
                    <button type="submit" class="btn btn-info">Submit</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { getAPI } from '../../axios-api'
    export default{
        name: 'DoctorsCreate',
        data () {
            return {
                firstname: '',
                lastname: '',
                gender:'',
                specialist:'',
                dayValue: [
                    {id: 1,value: "Sunday", name: 'Sunday', disabled: false, flag: 0},
                    {id: 2,value: "Monday", name: 'Monday', disabled: false, flag: 0},
                    {id: 3,value: "Tuesday", name: 'Tuesday', disabled: false, flag: 0},
                    {id: 4,value: "Wednesday", name: 'Wednesday', disabled: false, flag: 0},
                    {id: 5,value: "Thursday", name: 'Thursday', disabled: false, flag: 0},
                    {id: 6,value: "Friday", name: 'Friday', disabled: false, flag: 0},
                    {id: 7,value: "Saturday", name: 'Saturday', disabled: false, flag: 0},
                ],
            }
        },
        methods:{
            async submitForm() {
                const formData = {
                    firstName: this.firstname,
                    lastName: this.lastname,
                    gender: this.gender,
                    specialist: this.specialist
                }
                getAPI
                    .post('doctors/add_doctor',formData)
                    .then(response => {
                        console.log('Success')
                        console.log(response)
                        alert("Data Saved Successfully!")
                        this.$router.push('/doctorslist')
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