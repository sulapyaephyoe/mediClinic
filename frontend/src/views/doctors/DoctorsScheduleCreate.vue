<template>
    <div class="container">
        <div class="row">
            <div class="col-md-9 offset-md-1">
                <figure class="text-center">
                    <h3>Doctors' Schedule</h3>
                </figure>
                <form class="row g-3">
                    <!-- <div v-for="key in count" :key="key"> -->
                        <div class="col-md-4">
                            <label for="hospital" class="form-label">Hospital</label>
                            <input type="text" class="form-control" id="hospital" v-model="hospital">
                        </div>
                        <div class="col-md-3">
                            <label for="day" class="form-label">Day</label>
                            <select id="day" class="form-select" v-model="day">
                            <option selected>Choose...</option>
                            <option>...</option>
                            </select>
                        </div>
                        <div class="col-md-2">
                            <label for="startTime" class="form-label">Start Time</label>
                            <input type="text" class="form-control" id="startTime">
                        </div>
                        <div class="col-md-2">
                            <label for="endTime" class="form-label">End Time</label>
                            <input type="text" class="form-control" id="endTime">
                        </div>
                        <div class="col-md-1">
                            <label for="EndTime" class="form-label">Add New</label>
                            <button type="submit" class="btn btn-light" @click="add">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus-circle" viewBox="0 0 16 16">
                                <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                                <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
                                </svg>
                            </button>
                        </div>
                    <!-- </div> -->
                    <div class="col-12">
                        <button type="submit" class="btn btn-info">Submit</button>
                    </div>
                    <div v-for="key in count" :key="key">
                        <input type="text" v-model="values['dynamic-field-'+key]"  size="50" placeholder="Another Field" :id="key" >
                    </div>
                    <a href="#" id="add_more_fields" @click="add"><i class="fa fa-plus"></i> Add More</a>
                    <table class="table table-borderless">
                            <tr v-for="key in count" :key="key">
                                <td>
                                    <label for="startTime" class="form-label">Start Time</label>
                                    <input type="time" class="form-control" id="startTime">
                                </td>
                                <td>
                                    <label for="endTime" class="form-label">End Time</label>
                                    <input type="time" class="form-control" id="endTime">
                                </td>
                                <td>
                                    <label for="endTime" class="form-label">Add</label>
                                    <button type="submit" class="btn btn-light" @click="add">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus-circle" viewBox="0 0 16 16">
                                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                                        <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
                                        </svg>
                                    </button>
                                </td>
                                <td>
                                    <a href="#" id="add_more_fields" @click="add"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus-circle" viewBox="0 0 16 16">
                                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                                        <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
                                        </svg></a>
                                </td>
                            </tr>
                    </table>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    export default{
        name: 'DoctorsScheduleCreate',
        data () {
            return {
                hospital:'',
                days:[{ day: ''}],
                count: 1,
                values: {}
            }
        },
        methods: {
            // addField(value, fieldType) {
            //     fieldType.push({value:""})
            // },
            addField(object, fieldType) {
                let newObject ={};
                for (const [key, value] of Object.entries(object)) {
                    newObject[key]="";
                    console.log(value)
                }
                fieldType.push(newObject);
            },
            add: function(){
                this.count++
            },
            remove: function(){
                this.count--
            },
            submit: function(){
                for (var key of Object.keys(this.values)) {
                    console.log(key + " -> " + this.values[key])
                }
            }

        }
    }
</script>