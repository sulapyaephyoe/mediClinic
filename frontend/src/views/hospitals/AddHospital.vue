<template>
    <div class="container mt-5 mb-5">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h3 class="title text-center">Hospitals Create Form</h3>
            </div>
            <div id="alert"></div>
            <form @submit.prevent="submitForm">
                <div class="row" style="justify-content: center;">
                    <div class="col-md-6">
                        <div class="form-group mt-2">
                            <label for="name" class="form-label">Name</label>
                            <input type="text" class="form-control" placeholder="Enter name" v-model="name" id="name" required>
                        </div>
                        <div class="form-group mt-2">
                            <label for="phone" class="form-label">Phone</label>
                            <input type="tel" class="form-control" placeholder="Enter phone" v-model="phone" id="phone" pattern="[0-9]{9}" required>
                        </div>
                        <div class="form-group mt-2">
                            <label for="phone" class="form-label">Address</label>
                            <div class="row">
                                <!-- <div class="col">
                                    <input type="number" step="any" class="form-control" placeholder="Enter latitude" id="latitude" v-model="latitude" required>
                                </div>
                                <div class="col">
                                    <input type="number" step="any" class="form-control" placeholder="Enter longitude" id="longitude" v-model="longitude" required>
                                </div> -->
                                <div class="col">
                                    <input type="text" class="form-control" placeholder="Enter address" v-model="address" id="address" required>
                                </div>
                            </div>
                        </div>
                        <div class="form-group mt-2">
                            <label for="type" class="form-label">Photo</label>
                           <input type="file" class="form-control" name="myfile" ref="uploadphoto" @change="uploadPhoto" accept="image/*">
                        </div>
                        <div class="form-group mt-2">
                            <label for="type" class="form-label">Video</label>
                           <input type="file" class="form-control" name="myfile" ref="uploadvideo" @change="uploadVideo" accept="video/mp4,video/x-m4v,video/*">
                        </div>
                        <div class="form-group mt-2">
                            <label for="website" class="form-label">website</label>
                            <input type="text" class="form-control" placeholder="Enter website" v-model="website" id="website" required>
                        </div>
                        <div class="form-group mt-2">
                            <label for="type" class="form-label">Type</label>
                            <select class="form-select" aria-label="Default select example" v-model="type" id="type" required>
                                <option value="" disabled>Choose Type</option>
                                <option value="publichospital">Public Hospital</option>
                                <option value="privatehospital">Private Hospital</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <button class="btn-style-one mt-3" v-on:click="submitFile()">Add</button>
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
            address : '',
            website : '',
            type : '',
            photo : '',
            video : '',
        }
    },
    methods: {
        uploadPhoto(event) {
            this.photo = event.target.files[0]  
        },
        uploadVideo(event) {
            this.video = event.target.files[0]  
        },
        submitFile() {
                getAPI.post('hospitals/add_hospital',{
                name: this.name,
                phone: this.phone,
                address: this.address,
                website: this.website,
                type: this.type,
                photo: this.photo,
                video: this.video,
            },{
            headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then(response => {
                console.log(response)
                const elink = document.createElement('div');
                elink.setAttribute('class','alert alert-success')
                elink.innerHTML = 'New Hospital Added'
                console.log(elink)
                document.getElementById('alert').appendChild(elink)
                
                this.name = ''
                this.phone = ''
                this.address = ''
                this.website = ''
                this.type = ''
                this.$refs.uploadphoto.value = ''
                this.$refs.uploadvideo.value = ''
                
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