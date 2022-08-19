<template>
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
                <div class=".col-md-3 .offset-md-3 linkSchedule">
                    <!-- <router-link :to="{ name: 'DoctorsScheduleEditList', param: { id : doctor_info.id }}" class="btn btn-light" ><i class="bi bi-calendar2-plus"></i></router-link> -->
                </div>
                <figure class="text-center">
                    <h3>{{ hospital_info.name }}'s Schedule List</h3>
                </figure>
                <div v-if="doctors_schedule.length != 0">
                    <div class="table-wrapper-scroll-y my-custom-scrollbar">
                    <table class="table table-bordered shadow p-3 mb-5 bg-body rounded tblSchedule" id="MyTable">
                        <thead>
                            <tr>
                                <th class="thDay"></th>
                                <th v-for="day in dayValue" v-bind:key="day.id" class="thDay"> {{ day.name }} </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="time in dc_time" v-bind:key="time.id">
                                <td>{{ time }}</td>
                                <td v-for="day in dayValue" v-bind:key="day.id">
                                    <span v-for="schedule in doctors_schedule" v-bind:key="schedule.id" class="CellWithComment">
                                        <span
                                            v-if="schedule.startTime + '-' + schedule.endTime == time && schedule.day == day.value"  class="CellComment">
                                            {{ schedule.firstName }} {{ schedule.lastName }}<br>
                                            <p class="font-monospace">({{ schedule.specialist }})</p>
                                        </span>
                                    </span>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    </div>
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
                    <p class="font-monospace fs-3 lblNoSchedule">There Is No Schedule for {{ hospital_info.name }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { getAPI } from '../../axios-api'
export default {
    name: 'DoctorsSchedule',
    data() {
        return {
            doctor_v: '',
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
            hospital_info: {},
        }
    },
    mounted() {
        this.getOneSchedule()
    },
    methods: {
        async getOneSchedule() {
            const hospitalID = this.$route.params.id
            console.log(hospitalID)
            getAPI
                .post(`hospitals/doctor_schedule_list/${hospitalID}`)
                .then(response => {
                    console.log(response)
                    this.doctors_schedule = response.data[0]
                    // console.log(this.doctors_schedule)
                    for (var ds of this.doctors_schedule) {
                        this.doctors_time.push(ds.startTime + '-' + ds.endTime)
                    }
                    for (var i = 0; i < this.doctors_time.length; i++) {
                        var j = i + 1
                        if (this.doctors_time[i] != this.doctors_time[j]) {
                            this.dc_time.push(this.doctors_time[i])
                        }
                    }
                    // console.log(this.dc_time)
                    this.hospitals = response.data[1]
                    console.log(this.doctors)
                    for (var hospital of this.hospitals) {
                        if (hospital.id == hospitalID) {
                            this.hospital_info = hospital
                        }
                    }
                    console.log(this.hospital_info.name)
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
            console.log(event.target.selectedOptions[0].value)
            window.location.href = ('/hospitals/schedule_list/' + event.target.selectedOptions[0].value)
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

.form-select {
    background-color: rgb(245, 242, 242);
    width: 20%;
}

.lblNoSchedule {
    text-align: center;
    color: red;
}

.thDay {
    width: 10%;
    background-color: rgb(239, 229, 249);
}

.linkSchedule {
    margin-left: 80%;
}

/* table scroll
.my-custom-scrollbar {
    position: relative;
    height: 550px;
    overflow: auto;
}

.table-wrapper-scroll-y {
    display: block;
} */
</style>