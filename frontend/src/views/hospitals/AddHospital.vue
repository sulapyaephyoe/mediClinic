<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add Hospital</h1>
            </div>
            <div id="alert"></div>
            <form @submit.prevent="submitForm">
                <div class="row">
                    <div class="col-md-6">
                        <div class="form-group mt-2">
                            <label for="name" class="form-label">Name</label>
                            <input type="text" class="form-control" placeholder="Enter name" v-model="name" id="name" required>
                        </div>
                        <div class="form-group mt-2">
                            <label for="phone" class="form-label">Phone</label>
                            <input type="text" class="form-control" placeholder="Enter phone" v-model="phone" id="phone" required>
                        </div>
                        <div class="form-group mt-2">
                            <label for="phone" class="form-label">Location</label>
                            <div class="row">
                                <div class="col">
                                    <input type="number" step="any" class="form-control" placeholder="Enter latitude" id="latitude" v-model="latitude" required>
                                </div>
                                <div class="col">
                                    <input type="number" step="any" class="form-control" placeholder="Enter longitude" id="longitude" v-model="longitude" required>
                                </div>
                                <div class="col">
                                    <input type="text" class="form-control" placeholder="Enter address" v-model="address" id="address" required>
                                </div>
                            </div>
                        </div>
                        <div class="form-group mt-2">
                            <label for="website" class="form-label">website</label>
                            <input type="text" class="form-control" placeholder="Enter website" v-model="website" id="website" required>
                        </div>
                        <div class="form-group mt-2">
                            <label for="type" class="form-label">Type</label>
                            <select class="form-select" aria-label="Default select example" v-model="type" id="type" required>
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
                getAPI.post('hospitals/add_hospital',{
                    name: this.name,
                    phone: this.phone,
                    latitude: this.latitude,
                    longitude: this.longitude,
                    address: this.address,
                    website: this.website,
                    type: this.type
                })
                .then(response => {
                    this.APIData = response.data
                    const elink = document.createElement('div');
                    elink.setAttribute('class','alert alert-success')
                    elink.innerHTML = 'New Hospital Added'
                    console.log(elink)
                    document.getElementById('alert').appendChild(elink)
                    document.getElementById('name').innerHTML = ' '
                    document.getElementById('phone').innerHTML = ' '
                    document.getElementById('latitude').innerHTML = ' '
                    document.getElementById('longitude').innerHTML = ' '
                    document.getElementById('address').innerHTML = ' '
                    document.getElementById('website').innerHTML = ' '
                    document.getElementById('type').innerHTML = ' '
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