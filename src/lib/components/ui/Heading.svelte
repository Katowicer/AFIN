<script lang="ts">
	import type { Snippet } from 'svelte';
	let { children } = $props<{ children: Snippet }>();
</script>

<h2 class="mb-4 text-xl sm:text-2xl md:text-3xl lg:text-5xl">
	{@render children()}
</h2>
