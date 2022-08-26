<template>
  <div class="col-md-6 offset-md-3">
    <figure class="text-center">
      <h3>Come & Grab Our Tele Consulting Services</h3>
    </figure>
    <div v-if="!paidFor">
    <figure class="text-center">
      <h4>Booking Form</h4>
    </figure>
      <form @submit.prevent="submitForm">
        <div class="mb-3">
          <label for="doctor" class="form-label">Patient Name</label>
          <input type="text" class="form-control" id="patient" v-model="patient" placeholder="Enter Patient Name" required>
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input type="email" class="form-control" id="email" v-model="email" placeholder="Enter E-mail" required>
        </div>
        <div class="mb-3">
          <label for="phone" class="form-label">Phone Number</label>
          <input type="text" class="form-control" id="phone" v-model="phone" placeholder="Enter Phone Number" pattern="[0-9]{9}" required>
        </div>
        <div class="mb-3">
          <label for="doctor" class="form-label">Types of Doctor</label>
          <select class="form-select" aria-label="Default select example" v-model="doctor" required>
            <option disabled value="" >Please Select Doctor</option>
            <option v-for="doctor in doctorValue" 
            :key="doctor.id" :value="doctor.value">
                {{doctor.name}}
            </option>
          </select>
        </div>
        <div class="mb-3">
          <label for="datetime" class="form-label">Date Time</label>
          <input type="datetime-local" class="form-select" v-model="datetime" name="time_start" required>
        </div>
        <div class="mb-3">
          <label for="fees" class="form-label">Service</label>
          <select class="form-select" aria-label="Default select example" v-model="service" required>
            <option disabled value="" >Please Choose Service</option>
            <option v-for="service in serviceValue" 
            :key="service.id" :value="service.service">
              {{service.service}}
            </option>
          </select>
        </div>
        <div class="mb-3">
          <label for="fees" class="form-label">Consulting Fees</label>
          <select class="form-select" aria-label="Default select example" v-model="fees" required>
            <option disabled value="" >Please Select Service</option>
            <option v-for="fee in feeValue" 
            :key="fee.id" :value="fee.value">
                $ {{ fee.value }} : {{ fee.name }}
            </option>
          </select>
        </div>
        <div ref="paypal"><label for="fees" class="form-label">Please Choose Payment Method</label></div>
      </form>
    </div>
    <div v-if="paidFor">
      <p class="fs-3 text-center" style="margin-bottom: 50px;">Your Booking Is Complete</p>
      <router-link :to="{ name: 'HomePage'}" class="btn btn-light" style="margin:0 auto !important; margin-left: 38%;margin-bottom: 80%;">Back To Home Page</router-link>
    </div>
  </div>
</template>

<script>
import { getAPI } from '../../axios-api'
export default {
  name: "BookingCreate",

  data: function() {
    return {
      loaded: false,
      paidFor: false,
      feeValue: [
        {id: 1, value: 10, name: 'Basic Service'},
        {id: 1, value: 20, name: 'Regular Service'},
        {id: 2, value: 40, name: '24/7 Service'},
        {id: 3, value: 50, name: 'Fast Response Service'},
      ],
      serviceValue: [
        {id: 1, service: 'Phone Consultation'},
        {id: 2, service: 'Email Consultation'},
        {id: 3, service: 'Video Consultation'},
      ],
      doctorValue: [
        {id:1,value:'Cardiologist',name:'Cardiologist'},
        {id:2,value:'ENT doctor',name:'ENT doctor'},
        {id:3,value:'Infectious Disease',name:'Infectious Disease'},
        {id:4,value:'Dermatologist',name:'Dermatologist'},
        {id:5,value:'Gastroenterologist',name:'Gardiologist'},
        {id:6,value:'Urologist',name:'Urologist'},
      ],
      patient: '',
      email: '',
      phone: '',
      fees: '',
      doctor: '',
      datetime: '',
      service: '',
    };
  },
  mounted: function() {
    const script = document.createElement("script");
    script.src =
      "https://www.paypal.com/sdk/js?client-id=ARNRNvgJTH0oaRUrQUC-p-MgCXzIOl5T6um6YqdW7U9mkwzV-ZkfCtp9c0QH6dRWArJY85Yh3rLCT5Vu&vault=true";
    script.addEventListener("load", this.setLoaded);
    document.body.appendChild(script);
    var today = new Date().toISOString().slice(0, 16);         //Past Date Disabled
    document.getElementsByName("time_start")[0].min = today;
  },
  methods: {
    setLoaded: function() {
      this.loaded = true;
      window.paypal
        .Buttons({
          style: {
            size: 'medium',
            color: 'blue',
            shape: 'pill',
          },
          createOrder: (data, actions) => {
            return actions.order.create({
              purchase_units: [
                {
                  description: this.fees,
                  amount: {
                    currency_code: "USD",
                    value: this.fees
                  }
                }
              ]
            });
          },
          onApprove: async (data, actions) => {
            const order = await actions.order.capture();
            this.data;
            this.paidFor = true;
            console.log(order);
            console.log(this.patient)
            const formData = {
              patient: this.patient,
              email: this.email,
              phone: this.phone,
              doctortype: this.doctor,
              datetime: this.datetime,
              fee: this.fees,
              service: this.service
            }
            getAPI
              .post('booking/add_booking',formData)
              .then(response => {
                  console.log('Success')
                  console.log(response)
                  alert("Data Saved Successfully!")
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
          onError: err => {
            console.log(err);
            alert("Please Select Service Fees")
          }
        })
        .render(this.$refs.paypal);
    },
  
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

</style>