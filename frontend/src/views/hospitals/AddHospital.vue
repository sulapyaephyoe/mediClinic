<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add Hospital</h1>
            </div>
             <div class="">
                <form @submit.prevent="submitForm">
                   <div class="row">
                        <div class="col-md-6">
                            <div class="form-group mt-2">
                                <label for="name" class="form-label">Name</label>
                                <input type="text" class="form-control" placeholder="Enter name" v-model="name">
                            </div>
                            <div class="form-group mt-2">
                                <label for="phone" class="form-label">Phone</label>
                                <input type="text" class="form-control" placeholder="Enter phone" v-model="phone">
                            </div>
                            <div class="form-group mt-2">
                                <label for="location" class="form-label">Location</label>
                                <input type="text" class="form-control" placeholder="Enter location" v-model="location">
                            </div>
                            <div class="form-group mt-2">
                                <label for="website" class="form-label">website</label>
                                <input type="text" class="form-control" placeholder="Enter website" v-model="website">
                            </div>
                            <div class="form-group mt-2">
                                <label for="type" class="form-label">Type</label>
                                <select class="form-select" aria-label="Default select example" v-model="type">
                                    <option value="">Choose Type</option>
                                    <option value="publichospital">Public Hospital</option>
                                    <option value="privatehospital">Private Hospital</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <button class="btn btn-info mt-3">Submit</button>
                            </div>
                        </div>
                   </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import { getAPI } from '../../axios-api'

    export default {
        name: 'AddHospital',
        data() {
            return {
              name : '',
              phone : '',
              location : '',
              website : '',
              type : '',
            }
        },
        methods: {
            async submitForm() {
                console.log(this.type)
                getAPI.post('/hospital/',{
                    name: this.name,
                    phone: this.phone,
                    location: this.location,
                    website: this.website,
                    type: this.type

                })
                .then(response => {
                    this.APIData = response.data
                  
                })
                .catch(err => {
                    console.log(err)
                })

            }
        }
    }
</script>
<style scoped>
</style>