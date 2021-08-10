module.exports = {
	// set your styleguidist configuration here
	title: 'COVID-19 Vaccine Dashboard Front-end',
	// components: 'src/components/**/[A-Z]*.vue',
	// defaultExample: true,
	sections: [
	   {
	     name: 'Components',
	     components: 'src/components/**/[A-Z]*.vue'
	   },
	   {
		   name: 'Services',
		   content: 'src/services/docs.md'
	   },
	   {
		   name: 'Router',
		   content: 'src/router/docs.md'
	   }
	 ],
	// webpackConfig: {
	//   // custom config goes here
	// },
	exampleMode: 'expand'
}
