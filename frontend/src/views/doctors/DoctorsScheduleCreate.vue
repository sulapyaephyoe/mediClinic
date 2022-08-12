<template>
    <div class="container">
        <div class="row">
            <!-- <div class="col-md-8 offset-md-2"> -->
            <figure class="text-center">
                <h3>{{doctor.firstName}} {{doctor.lastName}}' Schedule</h3>
            </figure>
            <form class="row g-3" @submit.prevent="submitForm">
                <table class="table table-striped table-hover">
                    <tr v-for="key in items" :key="key">
                        <td>
                            <table class="table tblHospital">
                                <tr>
                                    <td colspan="4">
                                        <div class="input-group input-group-sm mb-3">
                                            <span class="input-group-text" id="inputGroup-sizing-sm">Hospital</span>
                                            <select id="day" class="form-select" v-model="values['hospital-'+key+'-']" @change="setSelectedHospital($event,key)" required>
                                                <option disabled value="">Please select hospital</option>
                                                <option v-for="hospital in hospitalValue" :disabled="hospital.disabled" 
                                                :key="hospital.id" :value="hospital.id">
                                                    {{hospital.name}}
                                                </option>
                                            </select>
                                        </div>
                                    </td>
                                    <td class="tdAdd">
                                        <div class="input-group input-group-sm mb-3">
                                            <a href="#" id="add_more_fields" @click="remove(key)" class="btn btn-light form-control">
                                                <i class="bi bi-trash"></i>
                                            </a>
                                        </div>
                                    </td>
                                </tr>
                                <tr v-for="day in sample[key]" :key="day">
                                    <td>
                                        <div class="input-group input-group-sm mb-3">
                                            <span class="input-group-text" id="inputGroup-sizing-sm">Day</span>
                                            <select id="day" class="form-select" v-model="values['day-'+key+','+day]" @change="setSelectedValue($event,key,day)" required>
                                                <option v-for="day in dayValue" :disabled="day.disabled" 
                                                :key="day.value" :value="day.value">
                                                    {{day.name}}
                                                </option>
                                            </select>
                                        </div>
                                    </td>
                                    <td>
                                        <div class="input-group input-group-sm mb-3">
                                            <span class="input-group-text" id="inputGroup-sizing-sm">Start Time</span>
                                            <input type="time" class="form-control" id="startTime" v-model="values['startTime-'+key+','+day]" required>
                                        </div>
                                    </td>
                                    <td>
                                        <div class="input-group input-group-sm mb-3">
                                            <span class="input-group-text" id="inputGroup-sizing-sm">End Time</span>
                                            <input type="time" class="form-control" id="endTime" v-model="values['endTime-'+key+','+day]" required>
                                        </div>
                                    </td>
                                    <td class="tdAdd">
                                        <div class="input-group input-group-sm mb-3">
                                            <a href="#" id="add_more_fields" @click="removeday(key,day)" class="btn btn-light form-control">
                                                <i class="bi bi-dash"></i>
                                            </a>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <div class="input-group input-group-sm mb-3">
                                            <a href="#" id="add_more_fields" @click="addday(key)" class="btn btn-light">
                                                <i class="bi bi-plus"></i>
                                            </a>
                                        </div>
                                    </td>
                                    <td colspan="3"></td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <a href="#" id="add_more_fields" @click="add" class="btn btn-light form-control">
                            <i class="bi bi-plus-square"></i>
                        </a>
                    </tr>
                </table>
                <div class="col-12">
                    <button type="submit" class="btn btn-info">Submit</button>
                    <!-- <a href="#" @click="submit">Console</a> -->
                </div>
            </form>
        </div>
    </div>
</template>

<script>
const getInitialItems = () => [1]
let itemid = getInitialItems().length + 1
let dayid = getInitialItems().length + 1

import { getAPI } from '../../axios-api'
    export default{
        name: 'DoctorsScheduleCreate',
        data () {
            return {
                count: 1,
                daycount: 1,
                values: {},
                daytime: {},
                doctor: {},
                hospitalArray: [],
                objArray: [],
                dayValue: [
                    {id: 1,value: "Sunday", name: 'Sunday', disabled: false, flag: 0},
                    {id: 2,value: "Monday", name: 'Monday', disabled: false, flag: 0},
                    {id: 3,value: "Tuesday", name: 'Tuesday', disabled: false, flag: 0},
                    {id: 4,value: "Wednesday", name: 'Wednesday', disabled: false, flag: 0},
                    {id: 5,value: "Thursday", name: 'Thursday', disabled: false, flag: 0},
                    {id: 6,value: "Friday", name: 'Friday', disabled: false, flag: 0},
                    {id: 7,value: "Saturday", name: 'Saturday', disabled: false, flag: 0},
                ],
                hospitalValue: [],
                selectedValue: [],
                items: getInitialItems(),
                dayItems: getInitialItems(),
                sample: [],
                selectedArray: [],
                selectedHospital: [0],
            }
        },
        mounted() {
            this.getDoctor()
            this.getHospital()
        },
        methods: {
            async getDoctor() {
                const doctorID = this.$route.params.id
                console.log(doctorID)
                this.sample[this.count]=[1]  //default
                getAPI
                    .get(`doctors/add_schedule/${doctorID}`)
                    .then(response => {
                        console.log(response)
                        this.doctor=response.data
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
            async getHospital() {
                getAPI
                    .get('doctors/get_hospital')
                    .then(response => {
                        this.hospitalValue=response.data
                        for(var i=0;i<this.hospitalValue.length;i++) {
                            this.hospitalValue[i]['disabled'] = false
                            this.hospitalValue[i]['flag'] = 0
                        }
                        console.log(this.hospitalValue)
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
                for (var x of this.items) {
                    for(var y of this.sample[x]) {
                        for (var key of Object.keys(this.values)) {
                            var a = key.length-3
                            var b = key.length-1
                            var c = key.length-2
                            if(key[c] == x) {
                                this.daytime['hospital_id'] = this.values[key] 
                                this.daytime['doctor_id'] = this.$route.params.id
                            }
                            if(key[a] == x && key[b] == y) {
                                if(key.match('day')) {
                                    this.daytime['day'] = this.values[key]
                                }else if(key.match('startTime')) {
                                    this.daytime['startTime'] = this.values[key]
                                }else if(key.match('endTime')) {
                                    this.daytime['endTime'] = this.values[key]
                                }
                            }
                        }
                        this.objArray.push(this.daytime)
                        this.daytime = {}
                    }
                }
                getAPI
                    .post('doctors/add_doctor_schedule', this.objArray)
                    .then (response => {
                        console.log('Success')
                        console.log(response)
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
            },
            add: function() {
                this.count++
                this.items.splice(this.count, 0, itemid++)
                //For Day Add
                this.selectedValue = []
                for(var dday of this.dayValue) {
                    dday.flag = 0
                    dday.disabled = false
                }
                this.sample[this.items[this.count-1]] = [1]
                this.daycount = 1
                dayid = 2
            },
            addday: function(key) {
                if(this.sample[key].length < 7) {
                    this.daycount++
                    this.sample[key].splice(this.daycount,0,dayid++)
                }
                console.log(this.sample[key])
            },
            remove: function(key) {
                const i = this.items.indexOf(key)
                this.count--
                if(this.count != 0){
                    if (i > -1) {
                        this.items.splice(i, 1)
                    }
                }
                for(var hospital of this.hospitalValue) {
                    if(hospital.id == this.values['hospital-'+key+'-']) {
                        hospital.flag = 0
                        hospital.disabled = false
                    }
                }
                this.selectedHospital[key]= 0
            },
            removeday: function(key,day) {
                try{
                    //deselect day 
                    for(var dday of this.dayValue) {
                        if(dday.value === this.values['day-'+key+','+day]){
                            dday.flag = 0
                            dday.disabled = false
                        }
                    }
                    // delete day record
                    var d = this.sample[key].indexOf(day)
                    console.log(d)
                    this.selectedArray[key][d] = ""
                    if(d > -1){
                        this.sample[key].splice(d, 1)
                    }
                }
                catch(e){
                    alert("Cannot Delete Empty Data! Please Fill The Data To Delete")
                }
            },
            setSelectedHospital: function(event,key) {
                this.selectedHospital[key] = event.target.selectedOptions[0].value
                console.log(event.target.selectedOptions[0].value)
                for(hospital of this.hospitalValue) {
                    hospital.flag = 0
                    hospital.disabled = false
                }
                for(var hospital of this.hospitalValue) {
                    for(var h of this.selectedHospital) {
                        if(hospital.id == h){
                            hospital.flag = 1
                        }
                    }
                }
                for(hospital of this.hospitalValue) {
                    if(hospital.flag == 1) {
                        hospital.disabled = true
                    }
                }
            },
            setSelectedValue: function(event,key,day) {
                this.selectedValue.splice(day-1,1,event.target.selectedOptions[0].value)
                this.selectedArray[key] = this.selectedValue
                console.log(this.selectedArray)
                for(ddd of this.dayValue) {
                    ddd.flag = 0
                    ddd.disabled = false
                }
                for(var eee of this.selectedArray[key]) {
                    for(var ddd of this.dayValue) {
                        if(ddd.value === eee) {
                            ddd.flag = 1
                        }
                    }
                }
                for(ddd of this.dayValue) {
                    if(ddd.flag == 1) {
                        ddd.disabled = true
                    }
                }
            },
        }
    }
</script>

<style scoped>
.tblHospital {
  border-bottom: 3px solid #eee;
}
.tdAdd {
    width: 5%;
}
.tdMinus {
    width: 5%;
}
</style>