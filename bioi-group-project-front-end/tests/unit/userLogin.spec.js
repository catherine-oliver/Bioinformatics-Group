import { expect } from 'chai'
import { shallowMount } from '@vue/test-utils'
import Login from '@/components/UserLogin.vue'

describe('CreateUser.vue', () => {
    let wrapper = null

    beforeEach(() => {
      wrapper = shallowMount(Login)
    })

    it('Loads the content of the page', () => {
      expect(wrapper.find('input[type=text]').exists()).to.be.true;
      expect(wrapper.find('input[type=password]').exists()).to.be.true;
      expect(wrapper.find('input[type=submit]').exists()).to.be.true;
    })

    it('Changes username data element after changing form', () => {
      wrapper.findAll('input[type=text]').at(0).setValue("testing")
      expect(wrapper.vm.username).equal('testing')
    })

    it("Changes password data element after changing form", () => {
      wrapper.find('input[type=password]').setValue("testPassword")
      expect(wrapper.vm.password).equal('testPassword')
    })

    it("Shows error message if password less than 5 characters", () => {
      wrapper.find('input[type=password]').setValue("test")
      wrapper.vm.$nextTick(() => {
        expect(wrapper.vm.msg['password']).equal('Password must be 8 characters long')
        expect(wrapper.find('span').isVisible()).to.be.true;
      })
    })


    


  })