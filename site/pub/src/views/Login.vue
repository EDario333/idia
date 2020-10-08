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
                  {{ $t('Or sign in with credentials') }}
                </small>
              </div>

              <form role="form">
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
                  @blur="pass.blur()"
                >
                  <template v-slot:helpBlock v-if="!pass.valid">
                    <div class="text-danger invalid-feedback mt-2 ml-2" style="display: block;">
                      {{ pass.error }}
                    </div>
                  </template>
                </base-input>

                <base-checkbox>
                  {{ $t('Remember me') }}
                </base-checkbox>

                <div class="text-center">
                  <base-button
                    v-if="!form.processing"
                    type="primary"
                    class="my-4"
                    :disabled="email.val.trim().length<1 || pass.val.trim().length<1"
                    @click="submit()"
                  >
                    {{ $t('actions.Login button short text') }}
                  </base-button>

                  <div
                    v-else
                    role="alert" 
                    class="alert alert-info alert-dismissible"
                  >                    
                    <span class="alert-inner--text">
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
                <span class="alert-inner--text">
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
              <a href="#" class="text-light">
                <small>
                  {{ $t('Forgot password') }}
                </small>
              </a>
            </div>

            <div class="col-6 text-right">
              <router-link to="/register" class="text-light">
              <!-- <a href="/register" class="text-light"> -->
                <small>
                  {{ $t('actions.Create account') }}
                </small>
              <!-- </a> -->
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
  import i18n from '@/i18n'
  import UsersDataService from '../services/UsersDataService'

  export default {
    data () {
      return {
        form: {
          valid: false,
          error: '',
          processed: false,
          processing: false,
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
          }
        },
        pass: {
          val: '',
          valid: undefined,
          error: '',
          blur () {
            this.valid = this.val.trim().length > 0
          },
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
    },
    methods: {
      checkForm () {
        this.form.valid = this.email.valid && this.pass.valid
      },
      submit () {
        this.form.error =  ''
        this.form.valid = true
        this.form.processing = true
        this.form.processed = false
        const data = { username: this.email.val, password: this.pass.val }
        UsersDataService.login(data)
          .then(response => {
            console.log("por aki")
            console.log(response)
            if (response.data.length<1) {
              
            }
            else {
              // this.form.valid = false
              // this.form.error = i18n.t('Specified email already exists')
              // this.form.processed = true
              // this.form.processing = false
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
                  UsersDataService.login(data)
                    .then(response => {
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
  };
</script>

<style>
</style>
