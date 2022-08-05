<template>
    <div class="container">
        <div class="row">
            <div class="col-md-6 offset-md-3">
                <figure class="text-center">
                    <h3>Doctors Create Form</h3>
                </figure>
                <form @submit.prevent="submitForm">
                    <div class="mb-3">
                        <label for="firstname" class="form-label">First Name</label>
                        <input type="text" class="form-control" id="firstname" v-model="firstname" required>
                    </div>
                    <div class="mb-3">
                        <label for="lastname" class="form-label">Last Name</label>
                        <input type="text" class="form-control" id="lastname" v-model="lastname" required>
                    </div>
                    <div class="mb-3">
                        <label for="gender" class="form-label">Gender</label>
                        <select class="form-select" aria-label="Default select example" v-model="gender" required>
                            <option selected disabled>Select Gender</option>
                            <option value="male">Male</option>
                            <option value="female">Female</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="specialist" class="form-label">Specialist</label>
                        <select class="form-select" aria-label="Default select example" v-model="specialist" required>
                            <option selected disabled>Select Specialist</option>
                            <option value="allergy and immunology">Allergy and immunology</option>
                            <option value="anesthesiology">Anesthesiology</option>
                            <option value="dermatology">Dermatology</option>
                            <option value="diagnostic radiology">Diagnostic radiology</option>
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
                specialist:''
            }
        },
        methods:{
            async submitForm(){
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