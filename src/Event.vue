<template>
    <div class="modal fade" :id="`exampleModal${event.id}`" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">{{ event.title }}</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form class="row" 
                            :id="`edit-appointment-form-${event.id}`" method="POST" action="/appointments">
                            <div class="col-12 p-1">
                                <label for="form-appointment">Appointment:</label>
                                <input type="text" name="title" required
                                    v-model="event.title"
                                    id="form-appointment" class="form-control form-control-sm">
                            </div>
                            <div class="col-12 p-1">
                                <label for="form-date">Date:</label>
                                <input type="date" name="date" required
                                    v-model="event.date"
                                    id="form-date" class="form-control form-control-sm">
                            </div>
                            <div class="col-12 p-1">
                                <label for="form-time">Time:</label>
                                <input type="time" name="time" required 
                                    v-model="event.time"
                                    id="form-time" class="form-control form-control-sm">
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-sm btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="submit" :form="`edit-appointment-form-${event.id}`" class="btn btn-sm btn-primary">Save</button>
                    </div>
                </div>
            </div>
        </div>
</template>
<script>
export default {
    name: "EventForm",

    props: {
        event: {
            type: Object,
            required: true,
        },
    },
}
</script>