<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <div class="row mt-5">
                    <div class="col-md-3">
                        <div class="select">
                            <select v-model="name" class="form-select rounded-pill" @change="choosedHName($event)" style="    background-color: rgb(245, 242, 242);width: 220px;" required>
                                <option disabled value="">Please select hospital</option>
                                <option v-for="l in list" v-bind:key="l.id" v-bind:value="l.name" selected
                                    id="mySelect">
                                    {{ l.name }}
                                </option>
                            </select>
                        </div>
                    </div>
                </div>
                <div class="row mt-5">
                    <div class="col-md-6">
                        <div class="card mb-3" id="card">
                            <div class="row g-0">
                                <div class="col-md-6">
                                    <div id="photo"></div>
                                </div>
                                <div class="col-md-6">
                                    <div class="card-body">
                                        <h5 class="card-title" id="hospitalname"></h5>
                                        <p class="card-text" id="hospitalphone"></p>
                                        <a class="card-text" id="hospitalwebsite" target="_blank"></a>
                                        <p class="card-text" id="hospitaltype"><small class="text-muted">Last updated 3
                                                mins ago</small></p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <iframe height="280" width="600" frameborder="0" id="video" allow='autoplay'></iframe>
                    </div>
                </div>
                <div class="row mt-3">
                    <div id="showmap"></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { getAPI } from '../../axios-api'

export default {
    name: 'ViewHospital',
    data() {
        return {
            map_data: {},
            list: [],
            name: '',
            hopital_data: [],
        }
    },
    created() {
        getAPI.get('/hospitals/get_hospital',)
            .then(response => {
                this.map_data = response.data
                this.list = response.data.list
                document.getElementById('showmap').innerHTML = response.data.map

                const i = 0
                document.getElementById('hospitalname').innerHTML = response.data.list[i].name
                document.getElementById('hospitalphone').innerHTML = response.data.list[i].phone
                document.getElementById('hospitalwebsite').innerHTML = response.data.list[i].website
                document.getElementById('hospitaltype').innerHTML = response.data.list[i].type

                // show photo
                const img = document.createElement('img')
                img.setAttribute('src', 'http://127.0.0.1:8000' + response.data.list[i].photo)
                img.setAttribute('class', 'img-fluid rounded-start')
                img.style.width = '395px'
                img.style.height = '250px'
                document.getElementById('photo').appendChild(img)
                // show video
                const video = document.getElementById('video')
                video.setAttribute('src', 'http://127.0.0.1:8000' + response.data.list[i].video)

                const link = document.getElementById('hospitalwebsite')
                link.href = response.data.list[i].website
                link.innerHTML = link
            })
            .catch(err => {
                console.log(err)
            })
    },
    methods: {
        choosedHName(event) {
            this.name = event.target.value
            document.getElementById('photo').innerHTML = ''
            document.getElementById('video').innerHTML = ''
            getAPI.post('/hospitals/get_map', {
                name: event.target.value
            })
            .then(response => {
                this.map_data = response.data
                document.getElementById('showmap').innerHTML = response.data.map

                for (var i = 0; i < response.data.hospital_data.length; i++) {
                    document.getElementById('hospitalname').innerHTML = response.data.hospital_data[i].name
                    document.getElementById('hospitalphone').innerHTML = response.data.hospital_data[i].phone
                    document.getElementById('hospitalwebsite').innerHTML = response.data.hospital_data[i].website
                    document.getElementById('hospitaltype').innerHTML = response.data.hospital_data[i].type

                    // show photo
                    const img = document.createElement('img')
                    img.setAttribute('src', 'http://127.0.0.1:8000' + response.data.hospital_data[i].photo)
                    img.setAttribute('class', 'img-fluid rounded-start')
                    img.style.width = '395px'
                    img.style.height = '250px'
                    document.getElementById('photo').appendChild(img)
                    // show video
                    const video = document.getElementById('video')
                    video.setAttribute('src', 'http://127.0.0.1:8000' + response.data.hospital_data[i].video)

                    const link = document.getElementById('hospitalwebsite')
                    link.href = response.data.hospital_data[i].website
                    link.innerHTML = link
                }
            })
            .catch(err => {
                console.log(err)
            })
        }
    }
}
</script>
<style scoped>
ul li:hover {
    background: aliceblue
}

#hospitalwebsite {
    color: black;
    text-decoration: none;
}

#hospitalwebsite:hover {
    text-decoration: underline;
}

#select {
    width: 420px;
    margin-left: 7px;
}
#showmap{
    height: 500px;
}
</style>