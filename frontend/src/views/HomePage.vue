<template>

  <head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
      integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  </head>
  <div id="carouselExampleIndicators" class="carousel slide img-height" data-ride="carousel"
    style="width:100%; height:650px !important;">
    <ol class="carousel-indicators">
      <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
      <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
      <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
    </ol>
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img class="d-block w-80 img-height" src="@/assets/images/slideImg1.jpg" alt="First slide">
      </div>
      <div class="carousel-item">
        <img class="d-block w-80 img-height" src="@/assets/images/slideImg2.jpg" alt="Second slide">
      </div>
      <div class="carousel-item">
        <img class="d-block w-80 img-height" src="@/assets/images/slideImg3.jpg" alt="Third slide">
      </div>
    </div>
    <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true" style="color:green"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true" style="color:green"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>
  <section class="cta">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <div class="cta-block">
            <div class="emmergency item">
              <i class="fa fa-phone"></i>
              <h2>Emegency Cases</h2>
              <a href="#">1-800-700-6200</a>
              <p>You can contact directly in emergency cases.</p>
            </div>
            <div class="top-doctor item">
              <i class="fa fa-stethoscope"></i>
              <h2>24 Hour Service</h2>
              <p>We are ready here to help you and don't hesitate to contact us.</p>
              <a href="#" class="btn btn-main">Read more</a>
            </div>
            <div class="working-time item">
              <i class="fa fa-hourglass-o"></i>
              <h2>Working Hours</h2>
              <ul class="w-hours">
                <li>Mon - Fri - <span>24 Hours</span></li>
                <li>Mon - Fri - <span>24 Hours</span></li>
                <li>Mon - Fri - <span>24 Hours</span></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <section class="feature-section section bg-gray">
    <div class="container">
      <div class="container marketing">

        <section class="pt-5 pb-5">
          <div class="container">
            <div class="row">
              <div class="col-6">
                <!-- <h3 class="mb-3">Carousel cards title </h3> -->
              </div>
              <div class="container marketing">

                <!-- Three columns of text below the carousel -->
                <div class="row circlepattern">
                  <div class="col-lg-4" v-for="ph in photo" v-bind:key="ph.id">
                      <img :src=ph.photo width="140" height="140" class="bd-placeholder-img rounded-circle">
                            <h3>{{ph.name}}</h3>
                            <p>Your healthy life is our mission. You can enquery us about our services and packages.</p>
                            <p>
                              <router-link to='/hospitals/view-hospital' class="btn btn-secondary" @click="setHID(3)" style="background: #48bdc5;border: 1px solid #48bdc5;">View
                                details &raquo;</router-link>
                            </p>
                  </div><!-- /.col-lg-4 -->
                </div><!-- /.row -->
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
  </section>
  <ContactUs />
</template>
    
<script>
import { getAPI } from '../axios-api'
import ContactUs from '@/components/ContactusComponent';
export default {
  name: 'HomePage',
  components: {
    ContactUs
   },
  data() {
    return {
      hospitals: [],
      photo: []
    }
  },
  mounted() {
    this.getHospitals()
  },
  methods: {
    setHID(hid) {
      localStorage.setItem('hid', hid)
    },
    async getHospitals() {
      getAPI
        .get('hospitals/hospitalslist')
        .then(response => {
          this.hospitals = response.data
          console.log(this.hospitals)
          for(var hpphoto of this.hospitals){
            var str ='http://localhost:8000'+hpphoto.photo
            hpphoto['photo'] = str
            this.photo.push(hpphoto)
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
.img-height {
  width: 100% !important;
  height: 650px !important;
  margin: 0 auto;
}

.carousel-control-next-icon {
  background-image: url(https://cdn-icons-png.flaticon.com/512/130/130884.png) !important;
}

.carousel-control-prev-icon {
  background-image: url(https://cdn-icons-png.flaticon.com/512/130/130882.png) !important;
}

.pattern {
  width: 80% !important;
  height: 600px !important;
  margin: 0px 150px 0px 150px !important;
  align-items: center;
  justify-content: center !important;

}

.circlepattern {
  width: 80% !important;
  height: 400px !important;
  margin: 0px 150px 0px 150px !important;
  align-items: center;
  justify-content: center !important;
}


/* Left contact page */
.form-horizontal {
  /*float: left;*/
  max-width: 400px;
  font-family: 'Lato';
  font-weight: 400;
}

.form-control,
textarea {
  width: 400px !important;
  background-color: #000;
  color: #fff;
  letter-spacing: 1px;
}


/* Begin Right Contact Page */
.direct-contact-container {
  max-width: 400px;
}

/* Location, Phone, Email Section */
.contact-list {
  list-style-type: none;
  margin-left: -30px;
  padding-right: 20px;
}

.list-item {
  line-height: 4;
  color: #aaa;
}

.contact-text {
  font: 300 18px 'Lato', sans-serif;
  letter-spacing: 1.9px;
  color: #bbb;
}

.send-button {
  width: 100px;
  height: 50px;
  margin: 0px 0px 0px 150px !important;
}

.place {
  margin-left: 62px;
}

.phone {
  margin-left: 56px;
}

.gmail {
  margin-left: 53px;
}

.contact-text a {
  color: #bbb;
  text-decoration: none;
  transition-duration: 0.2s;
}

.contact-text a:hover {
  color: #fff;
  text-decoration: none;
}

hr {
  border-color: rgba(255, 255, 255, .6);
}
</style>