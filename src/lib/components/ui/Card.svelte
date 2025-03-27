<script lang="ts">
	import type { Snippet } from 'svelte';

	let { children } = $props<{ children: Snippet }>();
</script>

<div
	class="flex items-center space-x-3 rounded-lg bg-white p-4 text-black shadow-md transition-all duration-1000 hover:-translate-y-1 hover:shadow-2xl"
>
	{@render children()}
</div>
