<template>
  <section class="section section-shaped section-lg my-0">
    <div class="shape shape-style-1 bg-gradient-default">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      <span></span>
    </div>

    <div class="container pt-lg-md">
      <div class="row justify-content-center">
        <div class="col-lg-5">
          <card
            type="secondary"
            shadow
            header-classes="bg-white pb-5"
            body-classes="px-lg-5 py-lg-5"
            class="border-0"
          >
            <template>
              <div class="text-muted text-center mb-3">
                <small>
                  {{ $t('Sign in with') }}
                </small>
              </div>

              <div class="btn-wrapper text-center">
                <!-- <base-button type="neutral">
                  <img slot="icon" src="img/icons/common/github.svg">
                  Github
                </base-button> -->

                <!-- <base-button type="neutral">
                  <img
                    slot="icon"
                    src="img/icons/common/google.svg"
                  />
                  Google
                </base-button> -->
                <g-signin-button
                  :params="googleSignInParams"
                  @success="onSignInSuccessGoogle"
                  @error="onSignInErrorGoogle"
                  class="btn btn-icon btn-neutral"
                >
                  <span style="margin-right: 10px">
                    <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="18px" height="18px" viewBox="0 0 48 48" class="abcRioButtonSvg">
                      <g>
                        <path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"></path>
                        <path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"></path>
                        <path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"></path>
                        <path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"></path>
                        <path fill="none" d="M0 0h48v48H0z"></path>
                      </g>
                    </svg>
                  </span>
                  Google
                </g-signin-button>

                <!-- <base-button type="neutral">
                  <i class="fa fa-facebook-square"></i> -->
                  <!-- <img
                    slot="icon"
                    src="img/icons/common/google.svg"
                  /> -->
                  <!-- Facebook
                </base-button> -->

                <fb-signin-button
                  :params="fbSignInParams"
                  @success="onSignInSuccessFB"
                  @error="onSignInErrorFB"
                  class="btn btn-icon btn-neutral"
                >
                  <i class="fa fa-facebook-square"></i>
                  Facebook
                </fb-signin-button>
              </div>
            </template>

            <template>
              <div class="text-center text-muted mb-4">
                <small>
                  {{ $t('Or sign up with credentials') }}
                </small>
              </div>

              <form role="form">
                <!-- <input
                  v-model="name.val"
                  alternative
                  class="mb-3"
                  :placeholder="$t('Name')"
                  :rules="name.rules"
                  addon-left-icon="ni ni-hat-3"
                  required
                />

                <v-text-field
                  v-model="name.val"
                  alternative
                  class="mb-3"
                  :placeholder="$t('Name')"
                  :rules="name.rules"
                  addon-left-icon="ni ni-hat-3"
                  required
                >
                </v-text-field> -->

                <!-- <input
                  v-model="name.val"
                  alternative
                  class="form-control mb-3"
                  :placeholder="$t('Name')"
                  :rules="name.rules"
                  addon-left-icon="ni ni-hat-3"
                  required
                /> -->

                <base-input
                  v-model="name.val"
                  alternative
                  class="mb-3"
                  :placeholder="$t('Name')"
                  addon-left-icon="ni ni-hat-3"
                  @blur="name.blur();checkForm()"
                  :valid="name.valid"
                >
                  <template v-slot:helpBlock v-if="!name.valid">
                    <div class="text-danger invalid-feedback mt-2 ml-2" style="display: block;">
                      {{ name.error }}
                    </div>
                  </template>
                </base-input>

                <base-input
                  v-model="email.val"
                  alternative
                  class="mb-3"
                  :placeholder="$t('E-mail')"
                  addon-left-icon="ni ni-email-83"
                  type="email"
                  @blur="email.blur();checkForm()"
                  :valid="email.valid"
                >
                   <template v-slot:helpBlock v-if="!email.valid">
                    <div class="text-danger invalid-feedback mt-2 ml-2" style="display: block;">
                      {{ email.error }}
                    </div>
                  </template>
                </base-input>

                <base-input
                  v-model="pass.val"
                  alternative
                  type="password"
                  :placeholder="$t('Password')"
                  addon-left-icon="ni ni-lock-circle-open"
                  :valid="pass.valid"
                  @blur="checkPasswords()"
                >
                  <template v-slot:helpBlock v-if="!pass.valid">
                    <div class="text-danger invalid-feedback mt-2 ml-2" style="display: block;">
                      {{ pass.error }}
                    </div>
                  </template>
                </base-input>

                <base-input
                  v-model="pass2.val"
                  alternative
                  type="password"
                  :placeholder="$t('Retype password')"
                  :valid="pass2.valid"
                  @blur="checkPasswords()"
                >
                  <template v-slot:helpBlock v-if="!pass2.valid">
                    <div class="text-danger invalid-feedback mt-2 ml-2" style="display: block;">
                      {{ pass2.error }}
                    </div>
                  </template>
                </base-input>

                <div class="text-muted font-italic">
                  <small>
                    {{ $t('Password strength') }}:
                    <span class="text-success font-weight-700">
                      strong
                    </span>
                  </small>
                </div>

                <base-checkbox
                  v-model="privacyPolicyAccepted"
                >
                  <span>
                    {{ $t('I agree with the', { article: $t('The female plural') }) }}
                    <a href="#" onclick="alert('TODO'); return false;">
                      {{ $t('Privacy Policy') }}
                    </a>
                  </span>
                </base-checkbox>

                <div class="text-center">
                  <base-button
                    v-if="!form.processing"
                    type="primary"
                    class="my-4"
                    :disabled="!form.valid"
                    @click="submit()"
                  >
                    {{ $t('actions.Create account') }}
                  </base-button>

                  <div
                    v-else
                    role="alert" 
                    class="alert alert-info alert-dismissible"
                  >
                    <!-- <span class="alert-inner--icon">
                      <i class="ni ni-like-2"></i>
                    </span>  -->
                    
                    <span class="alert-inner--text">
                      <!-- <strong>Danger!</strong> -->
                      {{ $t('Loading') }}...
                    </span>
                  </div>
                </div>
              </form>

              <div
                v-if="!form.valid && form.processed" 
                role="alert" 
                class="alert alert-danger alert-dismissible"
              >
                <!-- <span class="alert-inner--icon">
                  <i class="ni ni-like-2"></i>
                </span> -->
                
                <span class="alert-inner--text">
                  <!-- <strong>Danger!</strong> -->
                  {{ form.error }}
                </span>

                <button 
                  type="button" 
                  data-dismiss="alert" 
                  :aria-label="$t('actions.Close')" 
                  class="close"
                  @click="form.processed=false;form.valid=true"
                >
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
            </template>
          </card>

          <div class="row mt-3">
            <div class="col-6">
              <router-link to="/login" class="text-light">
                <small>
                  {{ $t('actions.Login button short text') }}
                </small>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
  // import { required, email } from "vuelidate/lib/validators"
  import i18n from '@/i18n'
  import UsersDataService from '../services/UsersDataService'
  // import BaseInput from "../components/BaseInput";

  export default {
    // components: {
    //   'base-input': BaseInput,
    // },
    data () {
      return {
        privacyPolicyAccepted: false,
        form: {
          valid: false,
          error: '',
          processed: false,
          processing: false,
        },
        name: {
          val: '',
          valid: undefined,
          error: '',
          blur () {
            this.valid = !!this.val && this.val.length < 11
            if (!this.valid)
              if (!(!!this.val))
                this.error = i18n.t('Required field')
              else if (this.val.length > 10)
                this.error = 'longitud'
          }
        },
        email: {
          val: '',
          valid: undefined,
          error: '',
          blur () {
            // The RegExp for email was taken from https://emailregex.com/ and
            // is the used in type=”email” from W3C
            this.valid = !!this.val && this.val.match(new RegExp(/^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/, 'i'))
            if (!this.valid) {
              if (!(!!this.val))
                this.error = i18n.t('Required field')
              else 
                this.error = i18n.t('Bad email addr')
            }
            else {
              UsersDataService.byEmail(this.val)
                .then(response => {
                  if (response.data.length>0) {
                    // this.form.valid = false
                    this.valid = false 
                    this.error = i18n.t('Specified email already exists')
                  }
                })
                .catch(e => {
                  // this.form.valid = false
                  // this.form.error = e.message
                  // this.form.processed = true
                  // this.form.processing = false
                })
            }
          }
        },
        pass: {
          val: '',
          valid: undefined,
          error: '',
        },
        pass2: {
          val: '',
          valid: undefined,
          error: ''
        },
        googleSignInParams: {
          client_id: '885662440357-92k6a467q4nq58t349k3k1jmb7pc9ksn.apps.googleusercontent.com'
        },
        fbSignInParams: {
          scope: 'email,user_likes',
          return_scopes: true
        },
      }
    },
    created () {

    },
    mounted () {

    },
    computed: {

    },
    watch: {
      privacyPolicyAccepted () {
        this.checkForm()
      }
    },
    methods: {
      checkPasswords () {
        var valid=this.pass.val.trim().length>0 && this.pass2.val.trim().length>0
        if (!valid) {
          if (this.pass.val.trim().length<1) {
            this.pass.valid = false
            this.pass.error = i18n.t('Required field')
          }
          else {
            this.pass.valid = true
            this.pass.error = ''
          }
          if (this.pass2.val.trim().length<1) {
            this.pass2.valid = false
            this.pass2.error = i18n.t('Required field')
          }
          else {
            this.pass2.valid = true
            this.pass2.error = ''
          }
          this.checkForm()
          return false
        }

        valid=this.pass.val==this.pass2.val
        this.pass.valid=valid
        this.pass2.valid=valid
        if (!valid)
          this.pass.error=i18n.t('Passwords does not match')
        this.pass2.error=this.pass.error
        this.checkForm()
      },
      checkForm () {
        // alert('entro')
        this.form.valid = this.name.valid && this.email.valid && this.pass.valid && this.privacyPolicyAccepted
      },
      submit () {
        this.form.error =  ''
        this.form.valid = true
        this.form.processing = true
        this.form.processed = false
        UsersDataService.byEmail(this.email.val)
          .then(response => {
            if (response.data.length<1) {
              const data = { username: this.email.val, email: this.email.val, password: this.pass.val }
              UsersDataService.create(data)
                .then(response => {
                  console.log("CREADO NVO")
                  UsersDataService.token(data)
                    .then(response => {
                      console.log("SET AUTH")
                      this.$cookies.set('auth', response.data)
                      document.location.href="http://localhost:8081"
                    })
                    .catch(e => {
                      this.form.valid = false
                      this.form.error = e.message
                      this.form.processed = true
                      this.form.processing = false
                    })
                  // sessionStorage.setItem("uname", googleUser.Rt.Bu)
                  // sessionStorage.setItem("social_login", true)
                })
                .catch(e => {
                  this.form.valid = false
                  this.form.error = e.message
                  this.form.processed = true
                  this.form.processing = false
                })
            }
            else {
              this.form.valid = false
              this.form.error = i18n.t('Specified email already exists')
              this.form.processed = true
              this.form.processing = false
            }
          })
          .catch(e => {
            this.form.valid = false
            this.form.error = e.message
            this.form.processed = true
            this.form.processing = false
          })
      },
      onSignInSuccessGoogle (googleUser) {
        // `googleUser` is the GoogleUser object that represents the just-signed-in user.
        // See https://developers.google.com/identity/sign-in/web/reference#users
        const profile = googleUser.getBasicProfile() // etc etc
        // console.log(googleUser)
        UsersDataService.byEmail(googleUser.Rt.Bu)  
          .then(response => {
            const data = { username: googleUser.Rt.Bu, email: googleUser.Rt.Bu, password: googleUser.Rt.Bu }
            this.form.processing = true
            // First time login, insert record...
            if (response.data.length<1) {
              UsersDataService.create(data)
                .then(response => {
                  console.log("CREADO")
                  UsersDataService.token(data)
                    .then(response => {
                      this.$cookies.config('1d', '', '', false, 'Lax')
                      this.$cookies.set('auth', response.data)
                      document.location.href="http://localhost:8081"
                    })
                    .catch(e => {
                      this.form.valid = false
                      this.form.error = e.message
                      this.form.processed = true
                      this.form.processing = false
                    })
                  // sessionStorage.setItem("uname", googleUser.Rt.Bu)
                  // sessionStorage.setItem("social_login", true)
                })
                .catch(e => {
                  this.form.valid = false
                  this.form.error = e.message
                  this.form.processed = true
                  this.form.processing = false
                })
            }
            else {
              UsersDataService.token(data)
                .then(response => {
                  // console.log("RESPONSE TOKEN EXISTENTE")
                  // console.log(response)
                  this.$cookies.config('1d', '', '', false, 'Lax')
                  this.$cookies.set('auth', response.data)
                  document.location.href='http://localhost:8081'
                })
                .catch(e => {
                  this.form.valid = false
                  this.form.error = e.message
                  this.form.processed = true
                  this.form.processing = false
                })
              // document.location.href="http://localhost:8081"
            }
          })
          .catch(e => {
            this.form.valid = false
            this.form.error = e.message
            this.form.processed = true
            this.form.processing = false
          })
      },
      onSignInErrorGoogle (error) {
        // `error` contains any error occurred.
        console.log('OH NOES', error)
      },
      onSignInSuccessFB (response) {
        FB.api('/me', dude => {
          console.log(`Good to see you, ${dude.name}.`)
        })
      },
      onSignInErrorFB (error) {
        console.log('OH NOES', error)
      }
    },
    // validations: {
    //   name: {
    //     val: { required },
    //   }
    // }
  };
</script>

<style>
  
</style>
