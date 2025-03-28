<script lang="ts">
	let { href, title, description, icon } = $props<{
		href: string;
		title: string;
		description: string;
		icon: any;
	}>();
</script>

<a
	{href}
	target="_blank"
	class="flex flex-col items-center rounded-lg border border-gray-200 bg-white p-4 shadow transition-all duration-300 hover:translate-1
	       hover:border-l-4 hover:border-l-black hover:bg-gray-50 hover:pb-5 hover:shadow-lg focus:ring-2 focus:ring-yellow-400 focus:outline-none
	sm:flex-row md:scale-110 lg:scale-125"
	aria-label={`${title}: ${description}`}
>
	<span aria-hidden="true" class="mb-2 sm:mr-4 sm:mb-0">
		{@render icon()}
	</span>

	<div class="text-center sm:text-left">
		<h2 class="text-lg font-medium text-gray-900">{title}</h2>
		<p class="text-sm text-gray-700">{description}</p>
	</div>
</a>
