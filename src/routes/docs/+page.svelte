<script>
	import PDFIcon from '$lib/components/icons/PDFIcon.svelte';
	import XlsxIcon from '$lib/components/icons/XLSXIcon.svelte';
	import FileCard from '$lib/components/ui/FileCard.svelte';
</script>

<section class="flex-col space-y-5 md:space-y-10">
	<FileCard
		title="Bilancio 2021"
		description="Dichiarazione di bilancio anno 2021"
		href="./docs/Bilancio2021.pdf"
		icon={PDFIcon}
	></FileCard>

	<FileCard
		title="Bilancio 2022"
		description="Dichiarazione di bilancio anno 2022"
		href="./docs/Bilancio2022.pdf"
		icon={PDFIcon}
	></FileCard>

	<FileCard
		title="Atto costitutivo"
		description="Atto costitutivo"
		href="./docs/Costitutivo.pdf"
		icon={PDFIcon}
	></FileCard>

	<FileCard
		title="Statuto costruttivo"
		description=""
		href="./docs/Statuto.pdf"
		icon={PDFIcon}
	></FileCard>

	<FileCard
		title="Tabella trasparenza 2022 (L.124-2014)"
		description=""
		href="./docs/Tabella.xlsx"
		icon={XlsxIcon}
	></FileCard>
</section>


