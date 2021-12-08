<template>
  <div class="section">
    <div class="container">
      <div class="columns is-mobile">
        <div class="box mx-auto">
          <form action="post" @submit="login">
            <!-- EMAIL -->
            <b-field
              label="Email"
              :type="email.type"
              :message="email.message"
            >
              <b-input
                v-model="email.value"
                type="email"
                maxlength="30"
              />
            </b-field>
            <!-- PASSWORD -->
            <b-field
              label="Password"
              :type="password.type"
              :message="password.message"
            >
              <b-input v-model="password.value" type="password" maxlength="30" />
            </b-field>
            <!-- SUBMIT -->
            <div class="buttons">
              <b-button native-type="submit" expanded type="is-info" @click="login">
                Login
              </b-button>
              <b-button expanded type="" @click="loginAnonymous">
                Continue as anonymous
              </b-button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<script>

export default {
  name: 'Login',

  data () {
    return {
      email: {
        value: '',
        type: '',
        message: ''
      },
      password: {
        value: '',
        type: '',
        message: ''
      }
    }
  },
  mounted () {
    if (localStorage.getItem('email')) {
      this.email.value = localStorage.getItem('email')
    }
  },
  methods: {
    async login (event) {
      event.preventDefault()
      this.email.type = this.email.value ? '' : 'is-danger'
      this.password.type = this.password.value ? '' : 'is-danger'
      this.email.message = this.email.value ? '' : 'Enter a valid email.'
      this.password.message = this.password.value ? '' : 'Enter a valid password.'

      if (!this.email.value || !this.password.value) {
        return false
      }

      const data = { email: this.email.value, password: this.password.value }
      const authenticated = await this.$store.dispatch('auth/login', data)
      if (authenticated) {
        this.password.type = 'is-success'
        this.email.type = 'is-success'
        localStorage.setItem('email', this.email.value)
        this.openSuccessToast()
        this.$router.push({ name: 'index' })
      } else {
        this.password.type = 'is-danger'
        this.email.type = 'is-danger'
        this.openFailToast()
      }
    },
    openFailToast () {
      this.$buefy.toast.open({
        duration: 2000,
        message: 'The email and the password didn\'t match.',
        position: 'is-top',
        type: 'is-danger'
      })
    },
    openSuccessToast () {
      this.$buefy.toast.open({
        duration: 2000,
        message: 'You are logged in !.',
        position: 'is-top',
        type: 'is-success'
      })
    },
    loginAnonymous () {
      this.$router.push({ name: 'index' })
    }
  }
}
</script>

<style>
.box {
  min-width: 50vw;
}
</style>
