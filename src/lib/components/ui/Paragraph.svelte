<script lang="ts">
	import type { Snippet } from 'svelte';
	let { children } = $props<{ children: Snippet }>();
</script>

<p class="mb-4 text-sm sm:text-base md:text-lg">
	{@render children()}
</p>
