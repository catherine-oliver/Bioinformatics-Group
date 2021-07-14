import axios from 'axios';


export default {
    async getVaccineData(vaccineParams) {
        let res = await axios.get(("http://127.0.0.1:5000/getVaccineData"), {params: {vaccineParams: vaccineParams}});
        return res;
    }
}