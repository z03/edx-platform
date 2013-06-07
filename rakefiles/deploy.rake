
desc "Build a properties file used to trigger autodeploy builds"
task :autodeploy_properties do
    # Packaging constants
    commit = (ENV["GIT_COMMIT"] || `git rev-parse HEAD`).chomp()[0, 10]
    package_name = "mitx"
    branch = (ENV["GIT_BRANCH"] || `git symbolic-ref -q HEAD`).chomp().gsub('refs/heads/', '').gsub('origin/', '')

    File.open("autodeploy.properties", "w") do |file|
        file.puts("UPSTREAM_NOOP=false")
        file.puts("UPSTREAM_BRANCH=#{branch}")
        file.puts("UPSTREAM_JOB=#{package_name}")
        file.puts("UPSTREAM_REVISION=#{commit}")
    end
end