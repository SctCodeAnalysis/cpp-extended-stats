import click

import cpp_ext_stats


@click.command()
@click.argument("repo_path", type=click.Path(exists=True))
@click.option("--report", default="report.xml",
              help="Path to xml file where the report will be created")
def main(repo_path, report):
    """
    Main function that calculates metrics for a given C/C++
    repository and creates report as XML file.
    """
    stats = cpp_ext_stats.CppExtStats(repo_path)

    with open(report, "w") as file:
        click.echo(stats.as_xml(), file=file)


if __name__ == '__main__':
    main()
