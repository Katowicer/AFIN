<script lang="ts">
	import type { Snippet } from 'svelte';
	let { author, children } = $props<{ author: string; children: Snippet }>();
</script>

<div
	class="mx-auto mb-4 rounded-t-3xl rounded-bl-3xl border-2 border-solid border-gray-300 bg-white px-6 py-2 text-black shadow-md transition-all duration-300 hover:-translate-y-1 hover:border-black hover:font-medium hover:shadow-xl"
>
	<blockquote class="italic">
		{@render children()}
	</blockquote>
	<cite class="block text-right not-italic">- {author}</cite>
</div>
