<script lang="ts">
	import type { Snippet } from 'svelte';
	let { children } = $props<{ children: Snippet }>();
</script>

<h1 class="mb-4 text-2xl font-bold sm:text-3xl md:text-4xl lg:text-7xl">{@render children()}</h1>
