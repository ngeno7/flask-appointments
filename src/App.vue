<template>
    <FullCalendar :options="calendarOptions">
        <template v-slot:eventContent="arg">
            <button 
                type="button" data-bs-toggle="modal" 
                :data-bs-target="`#exampleModal${arg.event.id}`"
                class="btn btn-sm">{{ `${arg.event.title} - ${arg.event.extendedProps.time}` }}</button>
        </template>
    </FullCalendar>
    <div v-for="event in events">
        <EventForm :event="event"/>
    </div>
</template>
<script>
import FullCalendar from '@fullcalendar/vue3';
import dayGridPlugin from '@fullcalendar/daygrid';
import interactionPlugin from '@fullcalendar/interaction';
import EventForm from "./Event.vue";
export default {
    name: "Calendar",

    data() {
        return {
            events: []
        };
    },

    computed: {

        calendarOptions() {

            return {
                plugins: [dayGridPlugin, interactionPlugin],
                initialView: 'dayGridMonth',
                events: this.events.map(event => ({ title: event.title, date: event.date, id: event.id, time: event.time })).sort()
            };
        },
    },

    components: {
        FullCalendar,
        EventForm,
    },

    mounted() {

        this.fetchEvents();
    },

    methods: {

        fetchEvents() {

            window.axios.get(`/appointments?json=1`).then(({ data }) => {
                this.events = data;
            }).catch(() => { })
        },
    },
}
</script>