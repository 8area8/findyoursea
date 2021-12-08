import 'setimmediate'
import { get, setupTest } from '@nuxt/test-utils'
// import { createLocalVue } from '@vue/test-utils'
// import Vuex from 'vuex'
// import axios from 'axios'

// const localvue = createLocalVue()
// localvue.use(Vuex)
// localvue.use(axios)
// let NuxtStore
// let store

// beforeAll(async () => {
//   const storePath = '@/.nuxt/store.js'
//   NuxtStore = await import(storePath)
// })

// beforeEach(async () => {
//   store = await NuxtStore.createStore()
// })

describe('GET /', () => {
  setupTest({ server: true })

  describe('When we have no access token', () => {
    localStorage.clear()
    it('redirect to the login page', async () => {
      const response = await get('/')
      expect(response.url).toContain('/login')
    })
  })

  describe('When we try to log in', () => {
    it('can retrieve a JWT from credentials', async () => {
      // const data = { email: '123@test.com', password: '1234' }
      // const get = new Promise((resolve, reject) => {
      //   resolve({ data: { accessToken: 'accessToken', refreshToken: 'refreshToken' }, status: 200 })
      // })
      // store._actions['auth/login'].$axios = { get }
      // const status = await store.dispatch('login', data)
      // expect(status).toBeTruthy()
      // expect(localStorage.getItem('accessToken')).toBeTruthy()
      // expect(localStorage.getItem('refreshToken')).toBeTruthy()
    })
  })

  test('can access the index with a JWT', () => {
    // define datas
    // use axios
    // verify access and refresh tokens
  })
  test('can refresh an old acess token', () => {
    // define datas
    // use axios
    // verify access and refresh tokens
  })
  test('fail to refresh an old access token - max retry is 1', () => {
    // define datas
    // use axios
    // verify access and refresh tokens
  })
})
