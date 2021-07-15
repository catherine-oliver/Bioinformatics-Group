import { expect } from 'chai'
import { shallowMount } from '@vue/test-utils'
import dataVis from '@/components/DataVisualization.vue'
import USAMap from '@/components/USAMap.vue'

describe('dataVisualization.vue', () => {
    let wrapper = null

    beforeEach(() => {
      wrapper = shallowMount(dataVis)
    })

    it('Loads the Map', () => {
      expect(wrapper.findComponent(USAMap).exists()).to.be.true
    })

    it('Does not submit without a state selected', () => {
      wrapper.find("button").trigger('submit')
      expect(wrapper.vm.vaxData.totalCount).equal('')
      expect(wrapper.vm.vaxData.vaxTypeCount).equal('')
      expect(wrapper.vm.vaxData.ageCount).equal('')
    })

    it('Places Data into parameter object upon button press', () => {
      wrapper.vm.stateAbbr = "NE"
      wrapper.vm.ages = "12-17"
      wrapper.vm.vaxType = "Pfizer"

      wrapper.find('button').trigger('submit')
    
      expect(wrapper.vm.vaccineParams.state).equal('NE')
      expect(wrapper.vm.vaccineParams.vaxType).equal('Pfizer')
      expect(wrapper.vm.vaccineParams.ages).equal('12-17')

    })

    it('Dropdown for ages adds data to variable', () => {

      wrapper.findAll('select').at(0).findAll('option').at(2).setSelected()
    
      expect(wrapper.vm.ages).equal('18-64')
    })

    


  })