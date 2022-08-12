import { createApp } from 'vue'
import App from './App.vue'
import router from './routes.js'
import store from './store'
import 'bootstrap/dist/css/bootstrap.min.css'
// import './styles.css'
import 'bootstrap-icons/font/bootstrap-icons.css'

/* import the bootstrap icons  */
// import 'bootstrap-icons/font/bootstrap-icons.css'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
library.add(faUserSecret)

createApp(App).component('font-awesome-icon', FontAwesomeIcon).use(store).use(router).mount('#app')