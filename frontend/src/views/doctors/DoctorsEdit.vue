<template>
    <div class="container mt-5 mb-5">
        <div class="row">
            <div class="col-md-6 offset-md-3">
                <figure class="text-center">
                    <h3>Doctors Edit Form</h3>
                </figure>
                <form @submit.prevent="submitForm">
                    <div class="mb-3">
                        <label for="firstname" class="form-label">First Name</label>
                        <input type="text" class="form-control" id="firstname" v-model="firstname" placeholder="Enter First Name" required>
                    </div>
                    <div class="mb-3">
                        <label for="lastname" class="form-label">Last Name</label>
                        <input type="text" class="form-control" id="lastname" v-model="lastname" placeholder="Enter Last Name" required>
                    </div>
                    <div class="mb-3">
                        <label for="gender" class="form-label">Gender</label>
                        <select class="form-select" aria-label="Default select example" v-model="gender" required>
                            <option disabled value="">Please select gender</option>
                            <option value="Male">Male</option>
                            <option value="Female">Female</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="specialist" class="form-label">Specialist</label>
                        <select class="form-select" aria-label="Default select example" v-model="specialist" required>
                            <option disabled value="">Please select specialist</option>
                            <option v-for="specialist in specialistValue" 
                            :key="specialist.value" :value="specialist.value">
                                {{specialist.name}}
                            </option>
                        </select>
                    </div>
                    <button type="submit" class="btn-style-one">Edit</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { getAPI } from '../../axios-api'
    export default{
        name: 'DoctorsEdit',
        data () {
            return {
                firstname: '',
                lastname: '',
                gender:'',
                specialist:'',
                doctor: {},
                specialistValue: [
                    {value: "Allergy And Immunology", name: "Allergy And Immunology"},
                    {value: "Anesthesiology", name: "Anesthesiology"},
                    {value: "Dermatology", name: "Dermatology"},
                    {value: "Diagnostic Radiology", name: "Diagnostic Radiology"},
                    {value: "Emergency Medicine", name: "Emergency Medicine"},
                    {value: "Family Medicine", name: "Family Medicine"},
                    {value: "Internal Medicine", name: "Internal Medicine"},
                ],
            }
        },
        mounted() {
            this.getDoctor()
        },
        methods: {
            async getDoctor() {
                const doctorID = this.$route.params.id
                getAPI
                    .get(`doctors/doctor_edit/${doctorID}`)
                    .then(response => {
                        console.log(response)
                        this.doctor = response.data
                        this.firstname = this.doctor['firstName']
                        this.lastname = this.doctor['lastName']
                        this.gender = this.doctor['gender']
                        this.specialist = this.doctor['specialist']
                    })
                    .catch(error => {
                        console.log(error)
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
                    firstName: this.firstname,
                    lastName: this.lastname,
                    gender: this.gender,
                    specialist: this.specialist
                }
                const doctorID = this.$route.params.id
                getAPI
                    .post(`doctors/doctor_update/${doctorID}`,formData)
                    .then(response => {
                        console.log('Success')
                        console.log(response)
                        alert("Data Updated Successfully!")
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