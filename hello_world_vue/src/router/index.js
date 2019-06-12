import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import QuestionAndChoice from '@/components/QuestionAndChoice'
import Test from '@/components/Test'

Vue.use(Router)

export default new Router({
  mode: 'hash',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/question',
      name: 'QuestionAndChoice',
      component: QuestionAndChoice
    },
    {
      path: '/test',
      name: 'Test',
      component: Test
    }
  ]
})
