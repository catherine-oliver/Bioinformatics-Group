import { expect } from 'chai'
import { shallowMount } from '@vue/test-utils'
import CreateUser from '@/components/CreateUser.vue'

describe('CreateUser.vue', () => {
    let wrapper = null

    beforeEach(() => {
      wrapper = shallowMount(CreateUser)
    })

    it('Loads the content', () => {
      expect(wrapper.find('input[type=text]').exists()).to.be.true;
      expect(wrapper.find('input[type=password]').exists()).to.be.true;
      expect(wrapper.find('input[type=file]').exists()).to.be.true;
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

    it("Shows error message if password less than 5 characters", async () => {
      wrapper.find('input[type=password]').setValue("test");
      await wrapper.vm.$forceUpdate()
        expect(wrapper.vm.msg['password']).equal('Password must be 8 characters long')
        expect(wrapper.findAll('span').at(0).isVisible()).to.be.true;
    })
    it("Shows error message if form error is toggled", async () => {
      wrapper.vm.msg["formError"] = "Test";
      await wrapper.vm.$forceUpdate()
        expect(wrapper.findAll('span').at(0).isVisible()).to.be.true;
    })
  })