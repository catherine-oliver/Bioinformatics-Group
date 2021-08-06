import axios from 'axios';

var local = ''

export default {
    async getVaccineData(vaccineParams) {
        let res = await axios.get((local + "/api/getVaccineData"), {params: {state: vaccineParams.state, ages: vaccineParams.ages, vaxType: vaccineParams.vaxType}});
        return res;
    }
}