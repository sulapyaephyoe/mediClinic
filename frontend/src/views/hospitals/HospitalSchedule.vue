<template>
    <link rel="stylesheet" href="https://unpkg.com/microtip/microtip.css" />
    <div class="container mt-5 mb-5">
        <div class="row justify-content-md-center">
            <div class="col col-lg-10">
                <select id="doctor" class="form-select rounded-pill" v-model="doctor_v" @change="changeSchedule($event)"
                    required>
                    <option disabled value="">Please select hospital</option>
                    <option v-for="hospital in hospitals" :key="hospital.id" :value="hospital.id">
                        {{ hospital.name }}
                    </option>
                </select>

                <figure class="text-center">
                    <h3 v-if="hospital_info.name != null">{{ hospital_info.name }}'s Schedule List</h3>
                    <h3 v-else>Hospital's Schedule List</h3>
                </figure>
                <div v-if="doctors_schedule.length != 0">
                    <table class="table table-bordered shadow p-3 mb-5 bg-body rounded tblSchedule">
                        <thead>
                            <tr>
                                <th class="thDay"></th>
                                <th v-for="day in dayValue" v-bind:key="day.id" class="thDay"> {{ day.name }} </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="time in dc_time" v-bind:key="time.id" style="max-height: 100px;">
                                <td>{{ time }}</td>
                                <td v-for="day in dayValue" v-bind:key="day.id">
                                    <span v-for="schedule in doctors_schedule" v-bind:key="schedule.id">
                                        <span
                                            v-if="schedule.startTime + '-' + schedule.endTime == time && schedule.day == day.value">
                                            <span
                                                v-if="schedule.startTime + '-' + schedule.endTime == time && schedule.day == day.value">
                                                <!-- {{schedule.firstName}} {{schedule.lastName}}
                                            <p class="font-monospace">( {{ schedule.specialist }} )</p> -->
                                                <button
                                                    v-bind:aria-label="schedule.firstName + ' ' + schedule.lastName + '\r(' + schedule.specialist + ')'"
                                                    class="aria-label" data-microtip-position="bottom" role="tooltip"
                                                    style="width: 120px;white-space: nowrap !important;margin-bottom: 2px;border-radius: 6px;">
                                                    {{ schedule.firstName }} {{ schedule.lastName }}
                                                </button>

                                            </span>
                                        </span>
                                    </span>
                                </td>
                            </tr>
                            <!-- <tr>
                            <td id="lblSchedule" colspan="8"></td>
                        </tr> -->
                        </tbody>
                    </table>
                </div>
                <div v-if="doctors_schedule.length == 0">
                    <table class="table table-bordered shadow p-3 mb-5 bg-body rounded tblSchedule">
                        <thead>
                            <tr>
                                <th class="thDay"></th>
                                <th v-for="day in dayValue" v-bind:key="day.id" class="thDay"> {{ day.name }} </th>
                            </tr>
                        </thead>
                    </table>
                    <p class="font-monospace fs-3 lblNoSchedule" v-if="hospital_info.name != null">There Is No Schedule for {{ hospital_info.name }}</p>
                    <p class="font-monospace fs-3 lblNoSchedule" v-else></p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { getAPI } from '../../axios-api'
export default {
    name: 'HospitalsSchduleList',
    data() {
        return {
            doctor_v: "",
            doctors_schedule: [],
            doctors_time: [],
            doctors: [],
            dc_time: [],
            hospitals: [],
            dayValue: [
                { id: 1, value: "Sunday", name: 'Sunday', disabled: false, flag: 0 },
                { id: 2, value: "Monday", name: 'Monday', disabled: false, flag: 0 },
                { id: 3, value: "Tuesday", name: 'Tuesday', disabled: false, flag: 0 },
                { id: 4, value: "Wednesday", name: 'Wednesday', disabled: false, flag: 0 },
                { id: 5, value: "Thursday", name: 'Thursday', disabled: false, flag: 0 },
                { id: 6, value: "Friday", name: 'Friday', disabled: false, flag: 0 },
                { id: 7, value: "Saturday", name: 'Saturday', disabled: false, flag: 0 },
            ],
            timeValue: [
                { id: 1, startTime: '10:00:00', endTime: '11:00:00' },
                { id: 2, startTime: '11:00:00', endTime: '12:00:00' },
                { id: 3, startTime: '12:00:00', endTime: '13:00:00' },
                { id: 4, startTime: '13:00:00', endTime: '14:00:00' },
            ],
            doctor_info: {},
            hospital_info: {},
        }
    },
    mounted() {
        this.getDoctorsSchedule()
    },
    methods: {
        async getDoctorsSchedule() {
            getAPI
                .get('hospitals/doctor_schedule_list')
                .then(response => {
                    console.log(response)
                    this.hospitals = response.data[1]
                })
                .catch(error => {
                    console.log('Fail')
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    }
                    else if (error.message) {
                        this.errors.push('Something went wrong. Please Try Again')
                        console.log(error.message)
                    }
                })
        },
        changeSchedule: function (event) {
            this.dc_time = []
            this.doctors_time = []
            const hospitalID = event.target.selectedOptions[0].value
            // this.$router.push('/hospitals/schedule_list/'+event.target.selectedOptions[0].value)
            getAPI
                .post(`hospitals/doctor_schedule_list/${hospitalID}`)
                .then(response => {
                    this.doctors_schedule = response.data[0]
                   
                    for (var ds of this.doctors_schedule) {
                        this.doctors_time.push(ds.startTime + '-' + ds.endTime)
                    }
    
                    for (var i = 0; i < this.doctors_time.length; i++) {
                        var j = i + 1
                        if (this.doctors_time[i] != this.doctors_time[j]) {
                            this.dc_time.push(this.doctors_time[i])
                        }
                    }
                   
                    this.hospitals = response.data[1]
                    for (var hospital of this.hospitals) {
                        if (hospital.id == hospitalID) {
                            this.hospital_info = hospital
                        }
                    }
                    if (this.doctors_schedule.length == 0) {
                        this.dc_time = []
                    }
                })
                .catch(error => {
                    console.log('Fail')
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    }
                    else if (error.message) {
                        this.errors.push('Something went wrong. Please Try Again')
                        console.log(error.message)
                    }
                })
        }
    }
}
</script>
<style scoped>
.tblSchedule {
    border: 1px solid #eee
}

.tblSchedule tr {
    height: 100px;
}

.tblSchedule th {
    text-align: center;
    padding-bottom: 3%;
}

.tblSchedule td {
    text-align: center;
    padding-top: 3%;
}
.lblNoSchedule {
    text-align: center;
    color: red;
}

.form-select {
    background-color: rgb(245, 242, 242);
    width: 20%;
}

.thDay {
    width: 10%;
    background-color: rgb(239, 229, 249);
}
</style>