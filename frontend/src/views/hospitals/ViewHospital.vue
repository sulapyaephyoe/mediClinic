<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">View Hospital</h1>
                <div class="row mt-5">
                    <div class="col-md-4">
                        <!-- <ul class="list-group">
                            <li v-for="l in list" :key="l.id" class="list-group-item">
                            <a v-on:click='choosedHName(l.name)'>{{ l.name }}</a></li>
                        </ul>  -->
                        <div class="select">
                            <select v-model="name" required @change="choosedHName($event)" class="form-control">
                                <option value="" disabled>Choose Hospital</option>
                                <option
                                    v-for="l in list" 
                                    v-bind:key="l.id"
                                    v-bind:value="l.id" selected id="mySelect"
                                >
                                    {{ l.name }}
                                </option>
                            </select>
                        </div>
                        <div class="card mt-5" style="width: 20rem;">
                            <div class="card-body">
                                <h5 class="card-title">Hospital Information</h5>
                                <h6 class="card-subtitle mb-2 text-muted" id="hospitalname"></h6>
                                <p class="card-text" id="hospitalphone"></p>
                                <p class="card-text" id="hospitalwebsite"></p>
                                <p class="card-text" id="hospitaltype"></p>
                                <a href="#" class="card-link">Link</a>
                            </div>
                        </div>               
                    </div>
                    <div class="col-md-8">
                        <div id="showmap"></div>
                    </div>
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
                map_data : {},
                list: [],
                name: '',
                hopital_data: [],
            }
        },
        created () {
            getAPI.get('/hospitals/get_hospital',)
            .then(response => {
                this.map_data = response.data
                this.list = response.data.list
                document.getElementById('showmap').innerHTML = response.data.map
            })
            .catch(err => {
                console.log(err)
            })
        },
        methods: {
            choosedHName(event) {
                this.name = event.target.value
                getAPI.post('/hospitals/get_map',{
                    name : event.target.value
                })
                .then(response => {
                    console.log(response.data.hospital_data)
                    this.map_data = response.data
                    this.hospital_data = response.data.hospital_data[0]
                    document.getElementById('showmap').innerHTML = response.data.map
                    document.getElementById('hospitalname').innerHTML = response.data.hospital_data[0].name
                    document.getElementById('hospitalphone').innerHTML = response.data.hospital_data[0].phone
                    document.getElementById('hospitalwebsite').innerHTML = response.data.hospital_data[0].website
                    document.getElementById('hospitaltype').innerHTML = response.data.hospital_data[0].type

                    const $select = document.querySelector('#mySelect');
                    $select.setAttribute('selected','')
                    console.log($select)
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
</style>