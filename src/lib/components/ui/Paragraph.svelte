<script lang="ts">
	import type { Snippet } from 'svelte';
	let { children } = $props<{ children: Snippet }>();
</script>

<div class="px-2 border-solid border-l-black hover:border-l-2 hover:pb-5 transition-all duration-500">
	<p class="mb-4 text-sm sm:text-base md:text-lg">
		{@render children()}
	</p>
</div>
