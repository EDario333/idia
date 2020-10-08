/*!

=========================================================
* Vue Argon Design System - v1.1.0
=========================================================

* Product Page: https://www.creative-tim.com/product/argon-design-system
* Copyright 2019 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/argon-design-system/blob/master/LICENSE.md)

* Coded by www.creative-tim.com

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import Argon from "./plugins/argon-kit";
import './registerServiceWorker'
import i18n from './i18n'
import GSignInButton from 'vue-google-signin-button'
import FBSignInButton from 'vue-facebook-signin-button'
// import Vuex from 'vuex'
// import sessHandler from "vue";

// sessHandler.use(Vuex)
// var sess = { access: undefined, refresh: undefined }
// new Vuex.Store({
//   sess
// })

import VueCookies from 'vue-cookies'
Vue.use(VueCookies)

Vue.use(GSignInButton)
Vue.use(FBSignInButton)

Vue.config.productionTip = false;
Vue.use(Argon);
export default new Vue({
  router,
  i18n,
  // sess,
  render: h => h(App)
}).$mount("#app");
