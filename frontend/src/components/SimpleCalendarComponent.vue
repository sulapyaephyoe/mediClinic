<template>
	<div id="app">
		<h1>My Calendar</h1>
    <calendar-view
        :events="events"
        :show-date="showDate"
     
        class="theme-default holiday-us-traditional holiday-us-official"
      />
      <calendar-view-header
          :header-props="headerProps"
          @input="setShowDate"
        />
		<!-- <calendar-view
			:events="events"
			:show-date="showDate"
			class="theme-default holiday-us-traditional holiday-us-official">
			<template #header="{ headerProps }">
				<calendar-view-header
					:header-props="headerProps"
					@input="setShowDate" /> -->
			
	</div>
</template>
<script>

	import CalendarMathMixin from "@/components/CalendarMathMixin"
  import CalendarView from "@/components/CalendarView"
  import CalendarViewHeader from "@/components/CalendarViewHeader"

	import "/node_modules/vue-simple-calendar/dist/style.css"
	// The next two lines are optional themes
	import "/node_modules/vue-simple-calendar/static/css/default.css"
	import "/node_modules/vue-simple-calendar/static/css/holidays-us.css"

	export default {
		name: 'app',
		data: function() {
			return { 
				showDate: new Date(),
        events: [
				{
					id: "e0",
					startDate: "2018-01-05",
				},
				{
					id: "e1",
					startDate: this.thisMonth(15, 18, 30),
				},
				{
					id: "e2",
					startDate: this.thisMonth(15),
					title: "Single-day item with a long title",
				},
				{
					id: "e3",
					startDate: this.thisMonth(7, 9, 25),
					endDate: this.thisMonth(10, 16, 30),
					title: "Multi-day item with a long title and times",
				},
				{
					id: "e4",
					startDate: this.thisMonth(20),
					title: "My Birthday!",
					classes: "birthday",
					url: "https://en.wikipedia.org/wiki/Birthday",
				},
				{
					id: "e5",
					startDate: this.thisMonth(5),
					endDate: this.thisMonth(12),
					title: "Multi-day item",
					classes: "purple",
				},
				{
					id: "foo",
					startDate: this.thisMonth(29),
					title: "Same day 1",
				},
				{
					id: "e6",
					startDate: this.thisMonth(29),
					title: "Same day 2",
					classes: "orange",
				},
				{
					id: "e7",
					startDate: this.thisMonth(29),
					title: "Same day 3",
				},
				{
					id: "e8",
					startDate: this.thisMonth(29),
					title: "Same day 4",
					classes: "orange",
				},
				{
					id: "e9",
					startDate: this.thisMonth(29),
					title: "Same day 5",
				},
				{
					id: "e10",
					startDate: this.thisMonth(29),
					title: "Same day 6",
					classes: "orange",
				},
				{
					id: "e11",
					startDate: this.thisMonth(29),
					title: "Same day 7",
				},
			],
			}
		},
		components: {
			CalendarView,
			CalendarViewHeader,
		},
    mixins: [CalendarMathMixin],
		methods: {
			setShowDate(d) {
				this.showDate = d
			},
      thisMonth(d, h, m){
        const t = new Date()
        return new Date(t.getFullYear(), t.getMonth(), d, h || 0, m || 0)
      }
		}
	}
</script>
<style>
	#app {
		font-family: 'Avenir', Helvetica, Arial, sans-serif;
		color: #2c3e50;
		height: 67vh;
		width: 90vw;
		margin-left: auto;
		margin-right: auto;
	}
</style>