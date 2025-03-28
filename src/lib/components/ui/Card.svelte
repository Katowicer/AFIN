<script lang="ts">
	import type { Snippet } from 'svelte';

	let { children } = $props<{ children: Snippet }>();
</script>

<div
	class="flex items-center space-x-3 rounded-lg border-solid border-l-black bg-white p-4 px-2 text-black shadow-md
	transition-all duration-500 hover:-translate-y-1 hover:border-l-4 hover:pb-5 hover:shadow-2xl"
>
	{@render children()}
</div>
